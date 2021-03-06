#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Providers configuration.

List here the video providers that should be used to match a video.

"""

LIVE_PROVIDERS = {
    'youtube': {
        'link_template': '//www.youtube.com/embed/'
                         '{video_id}?autoplay=1&rel=0',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://www.youtube.com/watch?v={video_id}',
        'matches': [
            r"""youtube.[a-z.]+/watch\?[^v]*v\=([^"'/&?@]+)""",
            r"""youtu.be/([^"'/&?@]+)""",
            r"""youtube.[a-z.]+/v/([^"'/&?@]+)""",
            r"""youtube.[a-z.]+/embed/(?!live_stream)([^"'/&?@]+)""",
        ]
    },
    'youtubechannel': {
        'link_template': '//www.youtube.com/embed/'
                         'live_stream?channel={video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://www.youtube.com/embed/'
                               'live_stream?channel={video_id}',
        'matches': [
            r"""youtube.[a-z.]+/embed/live_stream\?channel\=([^"'/&?@]+)""",
        ]
    },
    'facebookpage': {
        'link_template': 'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F{video_id}%2Flive%2F',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'https://www.facebook.com/{video_id}/live/',
        'matches': [
            r"""facebook.[a-z.]+/([^"'/&?@]+)/live/""",
        ]
    },
    'creacast': {
        'link_template': '//www.creacast.com/'
                         '{video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://www.creacast.com/{video_id}',
        'matches': [
            r"""creacast.[a-z.]+/([^"'/]+)""",
        ]
    },
    'piksel': {
        'link_template': '//player.piksel.com/'
                         '{video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://player.piksel.com/{video_id}',
        'matches': [
            r"""piksel.[a-z.]+/([^"'/]+)""",
        ]
    },
    'lightcastmedia': {
        'link_template': '//{video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': '{video_id}',
        'matches': [
            r"""([a-zA-Z0-9]+\.lightcastmedia.[a-z.]+/.+)""",
        ]
    },
    'facebook': {
        'link_template': '//www.facebook.com/video/embed?video_id={video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'https://www.facebook.com/video.php?v='
                               '{video_id}',
        'matches': [
            r"""facebook.[a-z.]+/watch/\?[^v]*v\=([^"'/&?@]+)""",
            r"""facebook.[a-z.]+/video.php\?[^v]*v\=([^"'/&?@]+)""",
            r"""facebook.[a-z.]+/video/embed\?video_id\=([^"'/&?@]+)""",
            r"""facebook.[a-z.]+/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+/([^"'/&?@]+)""",
        ]
    },
    'vimeo': {
        'link_template': '//player.vimeo.com/'
                         'video/{video_id}?autoplay=1',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://vimeo.com/{video_id}',
        'matches': [
            r"""vimeo.[a-z.]+/video/([^"'/&?@]+)""",
            r"""vimeo.[a-z.]+/moogaloop.swf\?clip_id=([^"'/&?@]+)""",
            r"""vimeo.[a-z.]+/[a-z]+/([^a-z"'/&?@]+)""",
            r"""vimeo.[a-z.]+/[a-z]+/[a-z]+/([^a-z"'/&?@]+)""",
            r"""vimeo.[a-z.]+/([^"'/&?@]+)""",
        ]
    },
}


PROVIDERS = {
    'youtube': {
        'link_template': '//www.youtube.com/embed/'
                         '{video_id}?autoplay=1&rel=0',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://www.youtube.com/watch?v={video_id}',
        'matches': [
            r"""youtube.[a-z.]+/watch\?[^v]*v\=([^"'/&?@]+)""",
            r"""youtu.be/([^"'/&?@]+)""",
            r"""youtube.[a-z.]+/v/([^"'/&?@]+)""",
            r"""youtube.[a-z.]+/embed/([^"'/&?@]+)""",
        ]
    },
    'vimeo': {
        'link_template': '//player.vimeo.com/'
                         'video/{video_id}?autoplay=1',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://vimeo.com/{video_id}',
        'matches': [
            r"""vimeo.[a-z.]+/video/([^"'/&?@]+)""",
            r"""vimeo.[a-z.]+/moogaloop.swf\?clip_id=([^"'/&?@]+)""",
            r"""vimeo.[a-z.]+/[a-z]+/([^a-z"'/&?@]+)""",
            r"""vimeo.[a-z.]+/[a-z]+/[a-z]+/([^a-z"'/&?@]+)""",
            r"""vimeo.[a-z.]+/([^"'/&?@]+)""",
        ]
    },
    'google': {
        'link_template': '//video.google.com/googleplayer.swf?'
                         'docId={video_id}&autoPlay=1&related=0',
        'embed_template': '<embed id=VideoPlayback src="{video_link}" '
                          'style="width:480px;height:395px" '
                          'allowfullscreen="true" '
                          'allowScriptAccess=always '
                          'type=application/x-shockwave-flash> </embed>',
        'validation_template': 'http://video.google.com/videoplay?'
                               'docid={video_id}',
        'matches': [
            r"""video.google.[a-z.]+/googleplayer.swf\?docId=([^"'/&?@]+)""",
        ]
    },
    'dailymotion': {
        'link_template': '//www.dailymotion.com/embed/video/{video_id}?'
                         'autoPlay=1&related=0',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://www.dailymotion.com/video/{video_id}',
        'matches': [
            r"""dailymotion.[a-z.]+/swf/video/([^"'/&?@]+)""",
            r"""dailymotion.[a-z.]+/swf/([^"'/&?@]+)""",
            r"""dailymotion.[a-z.]+/embed/video/([^"'/&?@]+)""",
            r"""dailymotion.[a-z.]+/video/([^"'/&?@_]+)(_.*)?""",
            r"""dai.ly/([^"'/&?@]+)""",
        ]
    },
    'crosstv': {
        'link_template': '//embed.cdn01.net/player.php?width=640&'
                         'height=360&tvButtonID=crosstv&autoPlay=1&'
                         'related=0&id={video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'http://embed.cdn01.net/player.php?width=640&'
                               'height=360&tvButtonID=crosstv&id={video_id}',
        'matches': [
            r"""embed.cdn01.[^/]+/player.php\?.*?&id=([^"'/&?@]+)""",
            r"""flashvars='.*?id=([^"'/&?@]+).*?tvButtonID=crosstv""",
        ]
    },
    'facebook': {
        'link_template': '//www.facebook.com/video/embed?video_id={video_id}',
        'embed_template': '<iframe width="480" height="395" '
                          'src="{video_link}" frameborder="0"></iframe>',
        'validation_template': 'https://www.facebook.com/video.php?v='
                               '{video_id}',
        'matches': [
            r"""facebook.[a-z.]+/watch/\?[^v]*v\=([^"'/&?@]+)""",
            r"""facebook.[a-z.]+/video.php\?[^v]*v\=([^"'/&?@]+)""",
            r"""facebook.[a-z.]+/video/embed\?video_id\=([^"'/&?@]+)""",
            r"""facebook.[a-z.]+/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+/([^"'/&?@]+)""",
        ]
    },
}
