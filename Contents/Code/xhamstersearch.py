# -*- coding: utf-8 -*-
XHAMSTER_SEARCH = '{0}/search.php?q={1}&qcat=video&page={2}'

################################################################################
@route(PREFIX+'/search', page = int)
def xhamster_search(query, page = 1):
  if XHAMSTER_DEBUG: Log.Info("[XHAMSTER] xhamster_search QUERY: " + query + " | PAGE: " + str(page) )

  oc = ObjectContainer(
    title2 = unicode(L('Search Results') + ': ' + query + ' | ' + L('Page') + ' ' + str(page))
  )

  noresults = ObjectContainer(
    title2 = unicode(L('Search Results') + ': ' + query + ' | ' + L('Page') + ' ' + str(page)),
    header   = L('no matching videos'),
    message  = L('no matching videos'),
    no_cache = True
  )

  search_query = String.Quote(query, usePlus=True)
  if XHAMSTER_DEBUG: Log.Info("[XHAMSTER] SEARCHING... " + search_query)
  url = XHAMSTER_SEARCH.format(XHAMSTER_BASE_URL, search_query, str(page))
  data = HTML.ElementFromURL( url )
  videos = data.xpath('//div[contains(@class, "video")]')

  if len(videos) > 0:
    for video in videos:
      if XHAMSTER_DEBUG: Log.Info(HTML.StringFromElement(video))
      video_url   = video.xpath('.//a/@href')[0]
      video_thumb = video.xpath('.//img/@src')[0]
      video_title = video.xpath('.//img/@alt')[0].strip()

      oc.add(VideoClipObject(
        url = video_url,
        title = video_title,
        thumb = Resource.ContentsOfURLWithFallback(url = video_thumb),
        art = Resource.ContentsOfURLWithFallback(url = video_thumb)
      ))

    next_a = data.xpath('//div[@class="pager"]//a[contains(@class,"last")]')
    if len(next_a) > 0:
      if XHAMSTER_DEBUG: Log.Info(HTML.StringFromElement(next_a[0]))
      oc.add(NextPageObject(
        key = Callback(
          xhamster_search,
          query = query,
          page = page + 1
        ),
        title = L('Next') + ' >>'
      ))

    return oc
  else:
    return noresults
