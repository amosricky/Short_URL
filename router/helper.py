from conf import conf
import urllib.parse as parse
import hashlib
import redis
import base62


def checkUrl(url):
    result = {"code": 200, "result": "", "message": ""}

    if len(url) > int(conf.config['system']['maxUrlLength']):
        result["code"] = 400
        result["message"] = "Please don't use url longer than 2000 character."
        return result

    parsed_url = parse.urlparse(url)
    if parsed_url.scheme == '':
        result["code"] = 400
        result["message"] = "Please use correct protocol such as 'http', 'https' or 'ftp'."
        return result
    return result


def short(url):
    hashStr = base62.encodebytes(hashlib.md5(url.encode(encoding='utf-8')).digest()[-5:])
    return hashStr


def getConnection():
    dbHost = conf.config['system']['dbHost']
    dbPort = conf.config['system']['dbPort']
    return redis.Redis(host=dbHost, port=int(dbPort))


def genShortUrl(url, conn):
    result = {"code": 200, "result": "", "message": ""}
    shortUrl = short(url)

    if conn.get(shortUrl) is not None:
        if conn.get(shortUrl).decode() == url:
            result["message"] = "ShortUrl already exist."
            result["result"] = conf.config['system']['defaultDomain'] + ":" + conf.config['system']['defaultPort'] + "/" + shortUrl
            return result
        else:
            result["message"] = "Collision."
            result["code"] = 500
            return result

    conn.set(shortUrl, url)
    result["result"] = conf.config['system']['defaultDomain'] + ":" + conf.config['system']['defaultPort'] + "/" + shortUrl
    return result


def getFullUrl(shortUrl, conn):
    result = {"code": 200, "result": "", "message": ""}
    if conn.get(shortUrl) is None:
        result["code"] = 400
        result["message"] = "Short Url not exist."
        return result
    else:
        result["result"] = conn.get(shortUrl).decode()
        return result