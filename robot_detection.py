from __future__ import print_function

import sys, os.path, codecs, re

robot_useragents = [
        'appie',
        'architext',
        'jeeves',
        'bjaaland',
        'contentmatch',
        'ferret',
        'googlebot',
        'google\-sitemaps',
        'gulliver',
        'virus[_+ ]detector',		# Must be before harvest
        'harvest',
        'htdig',
        'linkwalker',
        'lilina',
        'lycos[_+ ]',
        'moget',
        'muscatferret',
        'myweb',
        'nomad',
        'scooter',
        'slurp',
        '^voyager\/',
        'weblayers',
        # Common robots (Not in robot file)
        'antibot',
        'bruinbot',
        'digout4u',
        'echo!',
        'fast\-webcrawler',
        'ia_archiver\-web\.archive\.org', # Must be before ia_archiver to avoid confusion with alexa
        'ia_archiver',
        'jennybot',
        'mercator',
        'netcraft',
        'msnbot\-media',
        'msnbot',
        'petersnews',
        'relevantnoise\.com',
        'unlost_web_crawler',
        'voila',
        'webbase',
        'webcollage',
        'cfetch',
        'zyborg',	# Must be before wisenut 
        'wisenutbot'

        # Less common robots (In robot file)
        '[^a]fish',
        'abcdatos',
        'acme\.spider',
        'ahoythehomepagefinder',
        'alkaline',
        'anthill',
        'arachnophilia',
        'arale',
        'araneo',
        'aretha',
        'ariadne',
        'powermarks',
        'arks',
        'aspider',
        'atn\.txt',
        'atomz',
        'auresys',
        'backrub',
        'bbot',
        'bigbrother',
        'blackwidow',
        'blindekuh',
        'bloodhound',
        'borg\-bot',
        'brightnet',
        'bspider',
        'cactvschemistryspider',
        'calif[^r]',
        'cassandra',
        'cgireader',
        'checkbot',
        'christcrawler',
        'churl',
        'cienciaficcion',
        'collective',
        'combine',
        'conceptbot',
        'coolbot',
        'core',
        'cosmos',
        'cruiser',
        'cusco',
        'cyberspyder',
        'desertrealm',
        'deweb',
        'dienstspider',
        'digger',
        'diibot',
        'direct_hit',
        'dnabot',
        'download_express',
        'dragonbot',
        'dwcp',
        'e\-collector',
        'ebiness',
        'elfinbot',
        'emacs',
        'emcspider',
        'esther',
        'evliyacelebi',
        'fastcrawler',
        'feedcrawl',
        'fdse',
        'felix',
        'fetchrover',
        'fido',
        'finnish',
        'fireball',
        'fouineur',
        'francoroute',
        'freecrawl',
        'funnelweb',
        'gama',
        'gazz',
        'gcreep',
        'getbot',
        'geturl',
        'golem',
        'gougou',
        'grapnel',
        'griffon',
        'gromit',
        'gulperbot',
        'hambot',
        'havindex',
        'hometown',
        'htmlgobble',
        'hyperdecontextualizer',
        'iajabot',
        'iaskspider',
        'hl_ftien_spider',
        'sogou',
        'iconoclast',
        'ilse',
        'imagelock',
        'incywincy',
        'informant',
        'infoseek',
        'infoseeksidewinder',
        'infospider',
        'inspectorwww',
        'intelliagent',
        'irobot',
        'iron33',
        'israelisearch',
        'javabee',
        'jbot',
        'jcrawler',
        'jobo',
        'jobot',
        'joebot',
        'jubii',
        'jumpstation',
        'kapsi',
        'katipo',
        'kilroy',
        'ko[_+ ]yappo[_+ ]robot',
        'kummhttp',
        'labelgrabber\.txt',
        'larbin',
        'legs',
        'linkidator',
        'linkscan',
        'lockon',
        'logo_gif',
        'macworm',
        'magpie',
        'marvin',
        'mattie',
        'mediafox',
        'merzscope',
        'meshexplorer',
        'mindcrawler',
        'mnogosearch',
        'momspider',
        'monster',
        'motor',
        'muncher',
        'mwdsearch',
        'ndspider',
        'nederland\.zoek',
        'netcarta',
        'netmechanic',
        'netscoop',
        'newscan\-online',
        'nhse',
        'northstar',
        'nzexplorer',
        'objectssearch',
        'occam',
        'octopus',
        'openfind',
        'orb_search',
        'packrat',
        'pageboy',
        'parasite',
        'patric',
        'pegasus',
        'perignator',
        'perlcrawler',
        'phantom',
        'phpdig',
        'piltdownman',
        'pimptrain',
        'pioneer',
        'pitkow',
        'pjspider',
        'plumtreewebaccessor',
        'poppi',
        'portalb',
        'psbot',
        'python',
        'raven',
        'rbse',
        'resumerobot',
        'rhcs',
        'road_runner',
        'robbie',
        'robi',
        'robocrawl',
        'robofox',
        'robozilla',
        'roverbot',
        'rules',
        'safetynetrobot',
        'search\-info',
        'search_au',
        'searchprocess',
        'senrigan',
        'sgscout',
        'shaggy',
        'shaihulud',
        'sift',
        'simbot',
        'site\-valet',
        'sitetech',
        'skymob',
        'slcrawler',
        'smartspider',
        'snooper',
        'solbot',
        'speedy',
        'spider[_+ ]monkey',
        'spiderbot',
        'spiderline',
        'spiderman',
        'spiderview',
        'spry',
        'sqworm',
        'ssearcher',
        'suke',
        'sunrise',
        'suntek',
        'sven',
        'tach_bw',
        'tagyu_agent',
        'tailrank',
        'tarantula',
        'tarspider',
        'techbot',
        'templeton',
        'titan',
        'titin',
        'tkwww',
        'tlspider',
        'ucsd',
        'udmsearch',
        'universalfeedparser',
        'urlck',
        'valkyrie',
        'verticrawl',
        'victoria',
        'visionsearch',
        'voidbot',
        'vwbot',
        'w3index',
        'w3m2',
        'wallpaper',
        'wanderer',
        'wapspIRLider',
        'webbandit',
        'webcatcher',
        'webcopy',
        'webfetcher',
        'webfoot',
        'webinator',
        'weblinker',
        'webmirror',
        'webmoose',
        'webquest',
        'webreader',
        'webreaper',
        'websnarf',
        'webspider',
        'webvac',
        'webwalk',
        'webwalker',
        'webwatch',
        'whatuseek',
        'whowhere',
        'wired\-digital',
        'wmir',
        'wolp',
        'wombat',
        'wordpress',
        'worm',
        'woozweb',
        'wwwc',
        'wz101',
        'xget',
        # Other robots reported by users
        '1\-more_scanner',
        'accoona\-ai\-agent',
        'activebookmark',
        'adamm_bot',
        'almaden',
        'aipbot',
        'aleadsoftbot',
        'alpha_search_agent',
        'allrati',
        'aport',
        'archive\.org_bot',
        'argus', 		# Must be before nutch
        'arianna\.libero\.it',
        'aspseek',
        'asterias',
        'awbot',
        'baiduspider',
        'becomebot',
        'bender',
        'betabot',
        'biglotron',
        'bittorrent_bot',
        'biz360[_+ ]spider',
        'blogbridge[_+ ]service',
        'bloglines',
        'blogpulse',
        'blogsearch',
        'blogshares',
        'blogslive',
        'blogssay',
        'bncf\.firenze\.sbn\.it\/raccolta\.txt',
        'bobby',
        'boitho\.com\-dc',
        'bookmark\-manager',
        'boris',
        'bumblebee',
        'candlelight[_+ ]favorites[_+ ]inspector',
        'cbn00glebot',
        'cerberian_drtrs',
        'cfnetwork',
        'cipinetbot',
        'checkweb_link_validator',
        'commons\-httpclient',
        'computer_and_automation_research_institute_crawler',
        'converamultimediacrawler',
        'converacrawler',
        'cscrawler',
        'cse_html_validator_lite_online',
        'cuasarbot',
        'cursor',
        'custo',
        'datafountains\/dmoz_downloader',
        'daviesbot',
        'daypopbot',
        'deepindex',
        'dipsie\.bot',
        'dnsgroup',
        'domainchecker',
        'domainsdb\.net',
        'dulance',
        'dumbot',
        'dumm\.de\-bot',
        'earthcom\.info',
        'easydl',
        'edgeio\-retriever',
        'ets_v',
        'exactseek',
        'extreme[_+ ]picture[_+ ]finder',
        'eventax',
        'everbeecrawler',
        'everest\-vulcan',
        'ezresult',
        'enteprise',
        'facebook',
        'fast_enterprise_crawler.*crawleradmin\.t\-info@telekom\.de',
        'fast_enterprise_crawler.*t\-info_bi_cluster_crawleradmin\.t\-info@telekom\.de',
        'matrix_s\.p\.a\._\-_fast_enterprise_crawler', # must come before fast enterprise crawler
        'fast_enterprise_crawler',
        'fast\-search\-engine',
        'favicon',
        'favorg',
        'favorites_sweeper',
        'feedburner',
        'feedfetcher\-google',
        'feedflow',
        'feedster',
        'feedsky',
        'feedvalidator',
        'filmkamerabot',
        'findlinks',
        'findexa_crawler',
        'fooky\.com\/ScorpionBot',
        'g2crawler',
        'gaisbot',
        'geniebot',
        'gigabot',
        'girafabot',
        'global_fetch',
        'gnodspider',
        'goforit\.com',
        'goforitbot',
        'gonzo',
        'grub',
        'gpu_p2p_crawler',
        'henrythemiragorobot',
        'heritrix',
        'holmes',
        'hoowwwer',
        'hpprint',
        'htmlparser',
        'html[_+ ]link[_+ ]validator',
        'httrack',
        'hundesuche\.com\-bot',
        'ichiro',
        'iltrovatore\-setaccio',
        'infobot',
        'infociousbot',
        'infomine',
        'insurancobot',
        'internet[_+ ]ninja',
        'internetarchive',
        'internetseer',
        'internetsupervision',
        'irlbot',
        'isearch2006',
        'iupui_research_bot',
        'jrtwine[_+ ]software[_+ ]check[_+ ]favorites[_+ ]utility',
        'justview',
        'kalambot',
        'kamano\.de_newsfeedverzeichnis',
        'kazoombot',
        'kevin',
        'keyoshid', # Must come before Y!J
        'kinjabot',
        'kinja\-imagebot',
        'knowitall',
        'knowledge\.com',
        'kouaa_krawler',
        'krugle',
        'ksibot',
        'kurzor',
        'lanshanbot',
        'letscrawl\.com',
        'libcrawl',
        'linkbot',
        'link_valet_online',
        'metager\-linkchecker',	# Must be before linkchecker
        'linkchecker',
        'livejournal\.com',
        'lmspider',
        'lwp\-request',
        'lwp\-trivial',
        'magpierss',
        'mail\.ru',
        'mapoftheinternet\.com',
        'mediapartners\-google',
        'megite',
        'metaspinner',
        'microsoft[_+ ]url[_+ ]control',
        'mini\-reptile',
        'minirank',
        'missigua_locator',
        'misterbot',
        'miva',
        'mizzu_labs',
        'mj12bot',
        'mojeekbot',
        'msiecrawler',
        'ms_search_4\.0_robot',
        'msrabot',
        'msrbot',
        'mt::telegraph::agent',
        'nagios',
        'nasa_search',
        'mydoyouhike',
        'netluchs',
        'netsprint',
        'newsgatoronline',
        'nicebot',
        'nimblecrawler',
        'noxtrumbot',
        'npbot',
        'nutchcvs',
        'nutchosu\-vlib',
        'nutch',  # Must come after other nutch versions
        'ocelli',
        'octora_beta_bot',
        'omniexplorer[_+ ]bot',
        'onet\.pl[_+ ]sa',
        'onfolio',
        'opentaggerbot',
        'openwebspider',
        'oracle_ultra_search',
        'orbiter',
        'yodaobot',
        'qihoobot',
        'passwordmaker\.org',
        'pear_http_request_class',
        'peerbot',
        'perman',
        'php[_+ ]version[_+ ]tracker',
        'pictureofinternet',
        'ping\.blo\.gs',
        'plinki',
        'pluckfeedcrawler',
        'pogodak',
        'pompos',
        'popdexter',
        'port_huron_labs',
        'postfavorites',
        'projectwf\-java\-test\-crawler',
        'proodlebot',
        'pyquery',
        'rambler',
        'redalert',
        'rojo',
        'rssimagesbot',
        'ruffle',
        'rufusbot',
        'sandcrawler',
        'sbider',
        'schizozilla',
        'scumbot',
        'searchguild[_+ ]dmoz[_+ ]experiment',
        'seekbot',
        'sensis_web_crawler',
        'seznambot',
        'shim\-crawler',
        'shoutcast',
        'slysearch',
        'snap\.com_beta_crawler',
        'sohu\-search',
        'sohu', # "sohu agent"
        'snappy',
        'sphere_scout',
        'spip',
        'sproose_crawler',
        'steeler',
        'steroid__download',
        'suchfin\-bot',
        'superbot',
        'surveybot',
        'susie',
        'syndic8',
        'syndicapi',
        'synoobot',
        'tcl_http_client_package',
        'technoratibot',
        'teragramcrawlersurf',
        'test_crawler',
        'testbot',
        't\-h\-u\-n\-d\-e\-r\-s\-t\-o\-n\-e',
        'topicblogs',
        'turnitinbot',
        'turtlescanner',		# Must be before turtle
        'turtle',
        'tutorgigbot',
        'twiceler',
        'ubicrawler',
        'ultraseek',
        'unchaos_bot_hybrid_web_search_engine',
        'unido\-bot',
        'updated',
        'ustc\-semantic\-group',
        'vagabondo\-wap',
        'vagabondo',
        'vermut',
        'versus_crawler_from_eda\.baykan@epfl\.ch',
        'vespa_crawler',
        'vortex',
        'vse\/',
        'w3c\-checklink',
        'w3c[_+ ]css[_+ ]validator[_+ ]jfouffa',
        'w3c_validator',
        'watchmouse',
        'wavefire',
        'webclipping\.com',
        'webcompass',
        'webcrawl\.net',
        'web_downloader',
        'webdup',
        'webfilter',
        'webindexer',
        'webminer',
        'website[_+ ]monitoring[_+ ]bot',
        'webvulncrawl',
        'wells_search',
        'wonderer',
        'wume_crawler',
        'wwweasel',
        'xenu\'s_link_sleuth',
        'xenu_link_sleuth',
        'xirq',
        'y!j', # Must come after keyoshid Y!J
        'yacy',
        'yahoo\-blogs',
        'yahoo\-verticalcrawler',
        'yahoofeedseeker',
        'yahooseeker\-testing',
        'yahooseeker',
        'yahoo\-mmcrawler',
        'yahoo!_mindset',
        'yandex',
        'flexum',
        'yanga',
        'yooglifetchagent',
        'z\-add_link_checker',
        'zealbot',
        'zhuaxia',
        'zspider',
        'zeus',
        'ng\/1\.', # put at end to avoid false positive
        'ng\/2\.', # put at end to avoid false positive
        'exabot',  # put at end to avoid false positive
        # Other id that are 99% of robots
        'wget',
        'libwww',
        'java\/[0-9]'   # put at end to avoid false positive

        # Generic robot
        'robot',
        'checker',
        'crawl',
        'discovery',
        'hunter',
        'scanner',
        'spider',
        'sucker',
        'bot[\s_+:,\.\;\/\\\-]',
        '[\s_+:,\.\;\/\\\-]bot',
        'no_user_agent'

        # manually added
        'yeti',
        ]

robot_useragents = [re.compile(x) for x in robot_useragents]

def is_robot(user_agent):
    if not isinstance(user_agent, basestring):
        raise TypeError
    if len(user_agent) == 0:
        raise ValueError

    try:
        # See if any one matches
        return any(robot_ua.search(user_agent.lower()) for robot_ua in robot_useragents)
    except UnicodeDecodeError:
        # Unicode error, robot_useragents is unicode strings. user_agent might have malformed bytes, so try looking at boring ascii
        return any(robot_ua.search(user_agent.lower().encode('ascii', 'ignore')) for robot_ua in robot_useragents)



def _parse_db_export(filename):
    assert os.path.isfile(filename)

    lines = codecs.open(filename, encoding="latin1").readlines()

    exclude_ua = set()
    for line in lines:
        if line.startswith("robot-exclusion-useragent:"):
            line = line.strip()
            dont_care, ua = line.split(":", 1)
            ua = ua.strip()
            if ' or ' in ua:
                uas = ua.split(" or ")
                # remove quotes
                uas = [x[1:-1] if (x[0] in ['"', "'"] and x[-1] in ['"', "'"]) else x for x in uas]
            else:
                uas = [ua]
            for ua in uas:
                # don't include nonsense stuff
                if ua.lower() not in ['', '*', 'n/a', 'none', 'yes', 'no', "due to a deficiency in java it's not currently possible to set the user-agent."]:
                    exclude_ua.add(ua)

    if robot_useragents != exclude_ua:
        print("robot_detection is out of date. Here's the new robot_useragents variable:")
        print(exclude_ua)
    else:
        print("No changes, robot_detection is up to date")


if __name__ == '__main__' and len(sys.argv) == 2:
    _parse_db_export(sys.argv[1])

