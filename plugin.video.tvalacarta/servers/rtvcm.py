# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para rtvcm
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

from core import logger
from core import scrapertools

from lib import youtube_dl
import descargavideos

def get_video_url( page_url , premium = False , user="" , password="", video_password="", page_data="" ):
    logger.info("tvalacarta.server.rtvcm get_video_url page_url"+page_url)

    data = scrapertools.cache_page(page_url)
    #<iframe id="flumotion_iframe_player" name="flumotion_iframe_player" src="http://cdnapi.kaltura.com/p/2288691/sp/228869100/embedIframeJs/uiconf_id/39784151/partner_id/2288691?iframeembed=true&playerId=kaltura_player_1496914486&entry_id=0_7nkaf0ce&flashvars[streamerType]=auto"
    media_url = scrapertools.find_single_match(data,'<iframe id="flumotion_iframe_player" name="flumotion_iframe_player" src="([^"]+)"')

    video_urls = []

    ydl = youtube_dl.YoutubeDL({'outtmpl': u'%(id)s%(ext)s'})
    result = ydl.extract_info(media_url, download=False)
    logger.info("tvalacarta.server.rtvcm get_video_url result="+repr(result))

    if "ext" in result and "url" in result:
        video_urls.append(["[rtvcm]", scrapertools.safe_unicode(result['url']).encode('utf-8')+"|User-Agent=Mozilla/5.0"])
    else:

        if "entries" in result:
            for entry in result["entries"]:
                video_urls.append(["[rtvcm]", scrapertools.safe_unicode(entry['url']).encode('utf-8')+"|User-Agent=Mozilla/5.0"])

    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    return devuelve
