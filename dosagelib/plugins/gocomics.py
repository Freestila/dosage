# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher

from re import compile
from ..scraper import make_scraper
from ..util import tagre
from ..helpers import bounceStarter

_imageSearch = (
    compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[0-9a-fA-F]+)', before='alt="[0-9a-fA-F]+"')),
    compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[0-9a-fA-F]+)')),
    compile(tagre("meta", "content", r'(http://assets\.amuniversal\.com/[0-9a-fA-F]+)', before="og:image")),
)
_prevSearch = compile(tagre("a", "href", r'(/[^"]+/\d+/\d+/\d+)', after="prev"))
_nextSearch = compile(tagre("a", "href", r'(/[^"]+/\d+/\d+/\d+)', after="next"))

def add(name, shortname):
    # Unfortunately, the whole http://assets.amuniversal.com/ is blocked by
    # robots.txt, so we disable GoComics for now...
    return

    baseUrl = 'http://www.gocomics.com'
    url = baseUrl + shortname
    classname = 'GoComics_%s' % name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, day = pageUrl.rsplit('/', 3)
        return "%s_%s%s%s.gif" % (name, year, month, day)

    globals()[classname] = make_scraper(classname,
        url = url,
        starter = bounceStarter(url, _nextSearch),
        name='GoComics/' + name,
        stripUrl=baseUrl + shortname + '/%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help='Index format: yyyy/mm/dd',
        namer=namer,
    )

# old comics removed from the listing
add('AdventuresofDaisy', '/Adventures-of-Daisy')
add('AdventuresofMikeAndSimon', '/adventures-of-mike-and-simon')
add('AnythingGoes', '/anything-goes')
add('BarkingCrayon', '/barking-crayon')
add('BenAndSeymour', '/ben-seymour')
add('BestInShow', '/best-in-show')
add('BobtheGroanUP', '/bob-the-groanup')
add('Cartertoons', '/cartertoons')
add('CockroachComix', '/cockroachcomix')
add('CowSheepandaGnomeNamedHelga', '/cow-sheep-and-a-gnome-named-helga')
add('DabneyandDad', '/dabney-and-dad')
add('DialHforHBomb', '/dial-h-for-h-bomb')
add('DitzAbledPrincess', '/ditzabled-princess')
add('DoodleDaysComics', '/doodle-days')
add('Dragin', '/dragin')
add('EBEJeebie', '/ebe-jeebie')
add('EDITORIALPASTANDPRESENT', '/editorial-past-and-present')
add('ElephantintheRoom', '/elephant-in-the-room')
add('ElfandMotorbelly', '/elf-and-motorbelly')
add('EngagAndNevets', '/engag-nevets')
add('EttoreandBaldo', '/ettore-and-baldo')
add('FantasticMegaLeague', '/fantastiteam')
add('FarcesofNature', '/farces-of-nature')
add('Featherweight', '/featherweight')
add('FrizziToons', '/frizzitoons')
add('FundayMorning', '/funday-morning')
add('GetAGrip', '/get-a-grip')
add('GunstonStreet', '/gunston-street')
add('HanginOut', '/hangin-out')
add('HarambeeHills', '/harambeehills')
add('Hbenson7', '/hbenson7')
add('HeadComics', '/head-comics')
add('HeavenlyNostrils', '/heavenly-nostrils')
add('HolySchnark', '/holy-schnark!')
add('Humoresque', '/humoresque')
add('ImaDillo', '/i-m-a-dillo')
add('KozmooftheCosmos', '/kozmoofthecosmos')
add('LeGooseyLu', '/LeGoosey-Lu')
add('Leadbellies', '/leadbellies')
add('LostInTranslation', '/lost-in-translation')
add('LucasLuminous', '/lucas-luminous')
add('Markonpaper', '/mark-on-paper')
add('MaryBWary', '/mary-b-wary')
add('MidLifewAlan', '/mid-life-with-alan')
add('MixedMedications', '/mixedmedications')
add('MrMorris', '/mr-morris')
add('MyCage', '/mycage')
add('MyGuardianGrandpa', '/my-guardian-grandpa')
add('NeatStep', '/neatstep')
add('NedAndLarry', '/ned-and-larry')
add('NeighborhoodZone', '/neightborhood-zone')
add('NobodysHome', '/nobodys-home')
add('OntheQuad', '/on-the-quad')
add('OrangesareFunny', '/oranges-are-funny')
add('Outnumbered', '/outnumbered')
add('ParisDoodles', '/mo-willems-paris-doodles')
add('PetFood', '/pet-food')
add('PlentyofPenguins', '/plenty-of-penguins')
add('Putz', '/putz')
add('QuestionsForKids', '/questions-for-kids')
add('RogueSymmetry', '/rogue_symmetry')
add('SNAFU', '/snafu')
add('SPACESLUGS', '/spaceslugs')
add('STEPDAD', '/stepdad')
add('Sabine', '/sabine')
add('SecondPrize', '/secondprize')
add('Skooled', '/skooled')
add('SpaceNutz', '/space-nutz')
add('SpaceTimeFunnies', '/spacetimefunnies')
add('Stookie', '/Stookie')
add('SuburbanWilderness', '/suburban-wilderness')
add('SuckerHeadSmack', '/suckerhead-smack')
add('THESILVERLINING', '/silver-lining')
add('TOWHOMITMAYCONCERN', '/towhomitmayconcern')
add('TheAdventuresofTeetyBallerina', '/the-adventures-of-teety-ballerina')
add('TheEdperiment', '/the-edperiment')
add('TheFruitBowl', '/thefruitbowl')
add('TheGoldenKid', '/golden-kid')
add('TheLilMiesters', '/the-lil-miesters')
add('TheOdderLimits', '/the-odder-limits')
add('TheSingleDadDiaries', '/single-dad-diaries')
add('TheVernalPool', '/vernal-pool')
add('ThrompTM', '/thromp')
add('ToBeNamed', '/to-be-named')
add('TonyAuth', '/tonyauth')
add('Toocrazy', '/too-crazy')
add('WayOutInLeftField', '/Way-Out-In-Left-Field')
add('Whatcatscanandcantdo', '/whatcatscanandcantdo')
add('YouGuysAreMyFriendsTheComic', '/you-guys-are-my-friends')


# do not edit anything below since these entries are generated from scripts/update_plugins.sh
# DO NOT REMOVE
add('060', '/0-60')
add('2CowsandaChicken', '/2cowsandachicken')
add('5thYearSenior', '/5th-year-senior')
add('9ChickweedLane', '/9chickweedlane')
add('9to5', '/9to5')
add('ABitSketch', '/a-bit-sketch')
add('ABomb', '/a-bomb')
add('ABootsAndPupComic', '/a-boots-and-pup-comic')
add('ACMEINKD', '/acme-inkd')
add('APEanimalpuns4every1', '/ape')
add('AbnormalTruth', '/abnormal-truth')
add('AdamAtHome', '/adamathome')
add('AdmiralSquirt', '/admiral-squirt')
add('AdultChildren', '/adult-children')
add('AdventuresofMartyandTurkey', '/marty-and-turkey')
add('Agnes', '/agnes')
add('AlisonWard', '/alison-ward')
add('AlleyOop', '/alley-oop')
add('AmaZnEvents', '/amaznevents')
add('AmandatheGreat', '/amanda-the-great')
add('Andertoons', '/andertoons')
add('Andnow', '/and-now')
add('AndyCapp', '/andycapp')
add('Anecdote', '/anecdote')
add('AngryLittleGirls', '/angry-little-girls')
add('AnimalCrackers', '/animalcrackers')
add('Annie', '/annie')
add('AppleCreekComics', '/apple-creek')
add('ArloandJanis', '/arloandjanis')
add('AskShagg', '/askshagg')
add('AuntyAcid', '/aunty-acid')
add('BC', '/bc')
add('BCenEspaol', '/espanol/bcespanol')
add('BERSERKALERT', '/berserk-alert')
add('BUNS', '/buns')
add('BUSHYTALES', '/bushy-tales')
add('BackintheDay', '/backintheday')
add('BadReporter', '/badreporter')
add('Badlands', '/badlands')
add('Baldo', '/baldo')
add('BaldoenEspaol', '/espanol/baldoespanol')
add('BallardStreet', '/ballardstreet')
add('BananaTriangle', '/banana-triangle')
add('BarkeaterLake', '/barkeaterlake')
add('BarneyAndClyde', '/barneyandclyde')
add('BasicInstructions', '/basicinstructions')
add('BatchRejection', '/batch-rejection')
add('Bazoobee', '/bazoobee')
add('BeMisery', '/bemisery')
add('BeanietheBrownie', '/beanie-the-brownie')
add('Beardo', '/beardo')
add('Ben', '/ben')
add('BeneaththeFerns', '/beneath-the-ferns')
add('BenitinyEneas', '/espanol/muttandjeffespanol')
add('BergerAndWyse', '/berger-and-wyse')
add('BerkeleyMews', '/berkeley-mews')
add('Betty', '/betty')
add('Bewley', '/bewley')
add('BiffAndRiley', '/biff-and-riley')
add('BigNate', '/bignate')
add('BigNateFirstClass', '/big-nate-first-class')
add('BigTop', '/bigtop')
add('BillyAndCo', '/billy-and-co')
add('Biographic', '/biographic')
add('Birdbrains', '/birdbrains')
add('Bliss', '/bliss')
add('BloomCounty', '/bloomcounty')
add('BlueSkiesToons', '/blue-skies-toons')
add('Bluebonnets', '/cowsandstuff')
add('BoNanas', '/bonanas')
add('BobGorrell', '/bobgorrell')
add('BobtheSquirrel', '/bobthesquirrel')
add('Boogerbrain', '/boogerbrain')
add('Boomerangs', '/boomerangs')
add('Bork', '/bork')
add('BotBrothers', '/bot-brothers')
add('BottAuto', '/bott-auto')
add('Bottomliners', '/bottomliners')
add('BoundandGagged', '/boundandgagged')
add('BrainSquirts', '/brain-squirts')
add('BreakingCatNews', '/breaking-cat-news')
add('BreakofDay', '/break-of-day')
add('Brevity', '/brevity')
add('BrewsterRockit', '/brewsterrockit')
add('BrianMcFadden', '/brian-mcfadden')
add('BrilliantMines', '/brilliant-mines')
add('BroomHilda', '/broomhilda')
add('BuffaloChips', '/buffalo-chips')
add('Bully', '/bully')
add('Buni', '/buni')
add('BuzzaWuzza', '/buzza-wuzza')
add('CAFFEINATED', '/CAFFEINATED')
add('CafconLeche', '/cafeconleche')
add('CalAndOzz', '/cal-and-ozz')
add('CalvinandHobbes', '/calvinandhobbes')
add('CalvinandHobbesenEspaol', '/espanol/calvinandhobbesespanol')
add('CandacenCompany', '/candace-n-company')
add('Candorville', '/candorville')
add('CandyPills', '/candy-pills')
add('CapsulasMedicas', '/espanol/capsulas-medicas')
add('Cathy', '/cathy')
add('CatsAtWork', '/cats-at-work')
add('CestlaVie', '/cestlavie')
add('ChanLowe', '/chanlowe')
add('CharmysArmy', '/charmys-army')
add('ChasingUnicorns', '/chasing-unicorns')
add('CheapThrillsCuisine', '/cheap-thrills-cuisine')
add('ChipBok', '/chipbok')
add('ChrisBritt', '/chrisbritt')
add('ChubbyGirlComics', '/chubbygirlcomics')
add('ChuckleBros', '/chucklebros')
add('CitizenDog', '/citizendog')
add('Classifudds', '/classifudds')
add('ClayBennett', '/claybennett')
add('ClayJones', '/clayjones')
add('ClearBlueWater', '/clearbluewater')
add('Cleats', '/cleats')
add('CleoandCompany', '/cleo-and-company')
add('ClosetoHome', '/closetohome')
add('CoffeeShopTidbits', '/coffee-shop-tidbits')
add('ColonelKernel', '/colonel-kernel')
add('Committed', '/committed')
add('Computoon', '/compu-toon')
add('Condorito', '/espanol/condorito')
add('ConnietotheWonnie', '/connie-to-the-wonnie')
add('Cornered', '/cornered')
add('CourageousManAdventures', '/courageous-man-adventures')
add('CowTown', '/cowtown')
add('CowandBoyClassics', '/cowandboy')
add('CoyoteVille', '/coyteville')
add('Crooksville', '/crooksville')
add('Crumb', '/crumb')
add('CuldeSac', '/culdesac')
add('DBCartoons', '/db-cartoons')
add('DaddysHome', '/daddyshome')
add('DanWasserman', '/danwasserman')
add('DanaSummers', '/danasummers')
add('DarkSideoftheHorse', '/darksideofthehorse')
add('DarrinBell', '/darrin-bell')
add('DeepDarkFears', '/deep-dark-fears')
add('DevinCraneComicStripGhostwriter', '/devincranecomicstripghostwriter')
add('DiamondLil', '/diamondlil')
add('DickTracy', '/dicktracy')
add('DilbertClassics', '/dilbert-classics')
add('DilbertenEspaol', '/espanol/dilbert-en-espanol')
add('DiligentCity', '/diligent-city')
add('DinosaurComics', '/dinosaur-comics')
add('DogEatDoug', '/dogeatdoug')
add('DogsDucksandAliens', '/dogs-ducks-and-aliens')
add('DogsofCKennel', '/dogsofckennel')
add('DoingTime', '/doingtime')
add('DomesticAbuse', '/domesticabuse')
add('DonBrutus', '/espanol/don-brutus')
add('DontPicktheFlowers', '/dont-pick-the-flowers')
add('DoodleTown', '/doodle-town')
add('Doonesbury', '/doonesbury')
add('Drabble', '/drabble')
add('DrewSheneman', '/drewsheneman')
add('Dromo', '/dro-mo')
add('DudeandDude', '/dudedude')
add('DumbQuestionBadAnswer', '/dumb-question-bad-answer')
add('DustSpecks', '/dust-specks')
add('Econogirl', '/econogirl')
add('Eek', '/eek')
add('EightballEyeball', '/eightball-eyeball')
add('ElCafdePoncho', '/espanol/poochcafeespanol')
add('ElMundodeBeakman', '/beakmanespanol')
add('EleriMaiHarrisCartoons', '/eleri-mai-harris-cartoons')
add('Elmo', '/elmo')
add('EmmyLou', '/emmy-lou')
add('Endtown', '/endtown')
add('ErictheCircle', '/eric-the-circle')
add('EspressoCity', '/Espresso-City')
add('FMinus', '/fminus')
add('FacesoftheNewsbyKerryWaghorn', '/facesinthenews')
add('FamilyTree', '/familytree')
add('FarOut', '/far-out')
add('Farcus', '/farcus')
add('FatCats', '/fat-cats')
add('FleasonFlick', '/fleasonflick')
add('FloandFriends', '/floandfriends')
add('FoolishMortals', '/foolish-mortals')
add('ForBetterorForWorse', '/forbetterorforworse')
add('ForHeavensSake', '/forheavenssake')
add('FortKnox', '/fortknox')
add('FourEyes', '/four-eyes')
add('FoxTrot', '/foxtrot')
add('FoxTrotClassics', '/foxtrotclassics')
add('FoxTrotenEspaol', '/espanol/foxtrotespanol')
add('Francis', '/francis')
add('FrankAndErnest', '/frankandernest')
add('FrankAndSteinway', '/frank-and-steinway')
add('FrankBlunt', '/frankblunt')
add('FrankieComics', '/frankie-comics')
add('Frazz', '/frazz')
add('FredBasset', '/fredbasset')
add('FredBassetenEspaol', '/espanol/fredbassetespanol')
add('FreeRange', '/freerange')
add('FreshlySqueezed', '/freshlysqueezed')
add('FriedCritter', '/fried-critter')
add('FritzMurphyAndMulligan', '/fritz-murphy-and-mulligan')
add('FrogApplause', '/frogapplause')
add('FromtheMoWillemsSketchbook', '/from-the-mo-willems-sketchbook')
add('GIRTH', '/girth')
add('GarciaCartoonCo', '/garcia-cartoon-co')
add('Garfield', '/garfield')
add('GarfieldMinusGarfield', '/garfieldminusgarfield')
add('GarfieldenEspaol', '/espanol/garfieldespanol')
add('GaryMarkstein', '/garymarkstein')
add('GaryVarvel', '/garyvarvel')
add('GasolineAlley', '/gasolinealley')
add('GatorsAndSuch', '/gators-and-such')
add('Gaturro', '/espanol/gaturro')
add('Geech', '/geech')
add('GenerationMute', '/generation-mute')
add('GentleCreatures', '/gentle-creatures')
add('GetFuzzy', '/getfuzzy')
add('GetaLife', '/getalife')
add('GilThorp', '/gilthorp')
add('GingerMeggs', '/gingermeggs')
add('GingerMeggsenEspaol', '/espanol/gingermeggsespanol')
add('GlasbergenCartoons', '/glasbergen-cartoons')
add('GlennMcCoy', '/glennmccoy')
add('GoComicsontheRoad', '/gocomics-on-the-road')
add('Graffiti', '/graffiti')
add('GramDragon', '/gramdragon')
add('GrandAvenue', '/grand-avenue')
add('GrandmaSnoops', '/grandmasnoops')
add('GrannyAnny', '/granny-anny')
add('GrayMatters', '/gray-matters')
add('GreenHumour', '/green-humour')
add('GreenPieces', '/green-pieces')
add('HIP', '/hip')
add('HUBRIS', '/hubris')
add('HaikuEwe', '/haikuewe')
add('HalfFull', '/half-full')
add('HalfFullenEspaol', '/espanol/half-full-espanol')
add('HamShears', '/ham-shears')
add('HankandDalesOurWorld', '/hank-and-dales-our-world')
add('HanktheSock', '/hank-the-sock')
add('HaphazardHumor', '/haphazard-humor')
add('Headcheese', '/headcheese')
add('HealthCapsules', '/healthcapsules')
add('HeartoftheCity', '/heartofthecity')
add('Heathcliff', '/heathcliff')
add('HeathcliffenEspaol', '/espanol/heathcliffespanol')
add('HenryPayne', '/henrypayne')
add('HerbandJamaal', '/herbandjamaal')
add('Herman', '/herman')
add('HermanenEspaol', '/espanol/herman-en-espanol')
add('HipsterPicnic', '/hipster-picnic')
add('Hogwashed', '/hogwashed')
add('HolidayDoodles', '/holiday-doodles')
add('Hollywoodpecker', '/hollywoodpecker')
add('HomeandAway', '/homeandaway')
add('HugoComics', '/hugo-comics')
add('HumanCull', '/human-cull')
add('HumblebeeandBob', '/humblebee-and-bob')
add('HutchOwen', '/hutch-owen')
add('ImTellingMom', '/telling-mom')
add('ImagineThis', '/imaginethis')
add('InherittheMirth', '/inherit-the-mirth')
add('InkPen', '/inkpen')
add('InspectorDangersCrimeQuiz', '/inspector-dangers-crime-quiz')
add('IntheBleachers', '/inthebleachers')
add('IntheSticks', '/inthesticks')
add('InvisibleBread', '/invisible-bread')
add('IsleofEx', '/isle-of-ex')
add('ItsAllAboutYou', '/itsallaboutyou')
add('ItsjustJim', '/its-just-jim')
add('JackOhman', '/jackohman')
add('JackRadioComics', '/jack-radio-comics')
add('JanesWorld', '/janesworld')
add('JeffDanziger', '/jeffdanziger')
add('JeffStahler', '/jeffstahler')
add('JenSorensen', '/jen-sorensen')
add('JerryHolbert', '/jerryholbert')
add('JillpokeBohemia', '/jillpoke-bohemia')
add('JimAndSarah', '/jim-and-sarah')
add('JimBentonCartoons', '/jim-benton-cartoons')
add('JimMorin', '/jimmorin')
add('JimsJournal', '/jimsjournal')
add('JoeHeller', '/joe-heller')
add('JoeVanilla', '/joevanilla')
add('JoelPett', '/joelpett')
add('JohnDeering', '/johndeering')
add('JolleyStuffBrowser', '/jolleystuff-browser')
add('JordanandBentley', '/jordan-and-bentley')
add('JumpStart', '/jumpstart')
add('JustSayUncle', '/just-say-uncle')
add('JustoyFranco', '/espanol/justo-y-franco')
add('KartoonsByKline', '/kartoons-by-kline')
add('KatetheGreat', '/kate-the-great')
add('KenCatalino', '/kencatalino')
add('KevinKallaugher', '/kevinkallaugher')
add('KidBeowulf', '/kid-beowulf')
add('KidShayComics', '/kid-shay-comics')
add('KidSpot', '/kidspot')
add('KidTown', '/kidtown')
add('KirbysTreehouse', '/kirbys-treehouse')
add('KitNCarlyle', '/kitandcarlyle')
add('KitchenCapers', '/kitchen-capers')
add('Kliban', '/kliban')
add('KlibansCats', '/klibans-cats')
add('LIGHTERSIDE', '/lighter-side')
add('LaCucaracha', '/lacucaracha')
add('LaCucarachaenEspaol', '/espanol/la-cucaracha-en-espanol')
add('LaloAlcaraz', '/laloalcaraz')
add('LaloAlcarazenEspaol', '/espanol/laloenespanol')
add('LardWantsWorldPeace', '/lard-wants-world-peace')
add('LardsWorldPeaceTips', '/lards-world-peace-tips')
add('LarryvilleBlue', '/larryville-blue')
add('LasHermanasStone', '/espanol/stonesoup_espanol')
add('LastKiss', '/lastkiss')
add('LayLines', '/lay-lines')
add('LearntoSpeakCat', '/learn-to-speak-cat')
add('LegendofBill', '/legendofbill')
add('LeighLunaComics', '/leigh-luna-comics')
add('LibertyMeadows', '/libertymeadows')
add('LilAbner', '/lil-abner')
add('LiliandDerek', '/lili-and-derek')
add('Lio', '/lio')
add('LioenEspaol', '/espanol/lioespanol')
add('LisaBenson', '/lisabenson')
add('LittleDogLost', '/littledoglost')
add('LittleFriedChickenandSushi', '/little-fried-chicken-and-sushi')
add('LittleNemo', '/little-nemo')
add('Lola', '/lola')
add('LolaenEspaol', '/espanol/lola-en-espanol')
add('LooksGoodonPaper', '/looks-good-on-paper')
add('LooseParts', '/looseparts')
add('LosOsorios', '/espanol/los-osorios')
add('LostSheep', '/lostsheep')
add('LostSideofSuburbia', '/lostsideofsuburbia')
add('Luann', '/luann')
add('LuannAgainn', '/luann-againn')
add('LuannenEspaol', '/espanol/luannspanish')
add('Lucan', '/lucan')
add('LuckyCow', '/luckycow')
add('LugNuts', '/lug-nuts')
add('LumandAbner', '/lum-and-abner')
add('Mac', '/mac')
add('MadDogGhettoCop', '/maddogghettocop')
add('MagicinaMinute', '/magicinaminute')
add('Magnificatz', '/magnificatz')
add('Maintaining', '/maintaining')
add('MakingIt', '/making-it')
add('MariasDay', '/marias-day')
add('Marmaduke', '/marmaduke')
add('MarmadukeenEspaol', '/espanol/marmaduke-en-espanol')
add('MarshallRamsey', '/marshallramsey')
add('MassiveFalls', '/massive-falls')
add('MattBors', '/matt-bors')
add('MattDavies', '/mattdavies')
add('MattWuerker', '/mattwuerker')
add('Maximus', '/maximus')
add('McArroni', '/mcarroni')
add('MediumLarge', '/medium-large')
add('MegClassics', '/meg-classics')
add('MichaelRamirez', '/michaelramirez')
add('Mick', '/mick')
add('MikeLester', '/mike-lester')
add('MikeLuckovich', '/mikeluckovich')
add('MikeduJour', '/mike-du-jour')
add('Millennialhood', '/millennialhood')
add('Millennialville', '/millennialville')
add('Milton50', '/milton-5-0')
add('Mindframe', '/mindframe')
add('MinimumSecurity', '/minimumsecurity')
add('MiscSoup', '/misc-soup')
add('MisterAndMe', '/mister-and-me')
add('ModeratelyConfused', '/moderately-confused')
add('MollyandtheBear', '/mollyandthebear')
add('Momma', '/momma')
add('Mongrels', '/mongrels')
add('MonstersR4Real', '/monsters-r4-real')
add('Monty', '/monty')
add('MontyDiaros', '/espanol/monty-diarios')
add('Mortimer', '/mortimer')
add('MortsIsland', '/noahs-island')
add('MotleyClassics', '/motley-classics')
add('MrGigiandtheSquid', '/mr-gigi-and-the-squid')
add('Mulligan', '/mulligan')
add('MustardandBoloney', '/mustard-and-boloney')
add('MuttAndJeff', '/muttandjeff')
add('MyCageClassics', '/mycage')
add('MythTickle', '/mythtickle')
add('NEUROTICA', '/neurotica')
add('Nancy', '/nancy')
add('NancyClassics', '/nancy-classics')
add('NateelGrande', '/espanol/nate-el-grande')
add('NavyBean', '/navybean')
add('NestHeads', '/nestheads')
add('NewAdventuresofQueenVictoria', '/thenewadventuresofqueenvictoria')
add('NickAnderson', '/nickanderson')
add('NickandZuzu', '/nick-and-zuzu')
add('NoBusinessIKnow', '/nobusinessiknow')
add('NoOrdinaryLife', '/no-ordinary-life')
add('NoPlaceLikeHolmes', '/no-place-like-holmes')
add('NonSequitur', '/nonsequitur')
add('Norman', '/Norman')
add('NothingisNotSomething', '/nothing-is-not-something')
add('ONIONAndPEA', '/onion-and-pea')
add('Oat', '/oat')
add('ObamaandtheFatman', '/obama-and-the-fatman')
add('OfftheMark', '/offthemark')
add('OhBrother', '/oh-brother')
add('OllieandQuentin', '/ollie-and-quentin')
add('OnAClaireDay', '/onaclaireday')
add('OneBigHappy', '/onebighappy')
add('OrdinaryBill', '/ordinary-bill')
add('OriginsoftheSundayComics', '/origins-of-the-sunday-comics')
add('OutoftheGenePoolReRuns', '/outofthegenepool')
add('OverQuirked', '/over-quirked')
add('Overboard', '/overboard')
add('OverboardenEspaol', '/espanol/overboardespanol')
add('OvertheHedge', '/overthehedge')
add('OzyandMillie', '/ozy-and-millie')
add('PCandPixel', '/pcandpixel')
add('PaddedCell', '/padded-cell')
add('PamosWorld', '/pamos-world')
add('PatOliphant', '/patoliphant')
add('PaulSzep', '/paulszep')
add('PawsForThoughtComics', '/paws-for-thought-comics')
add('Peanizles', '/peanizles')
add('Peanuts', '/peanuts')
add('PeanutsBegins', '/peanuts-begins')
add('PeanutsenEspaol', '/espanol/peanuts-espanol')
add('PearlsBeforeSwine', '/pearlsbeforeswine')
add('Peeples', '/peeples')
add('Periquita', '/espanol/periquita')
add('PerlasparalosCerdos', '/espanol/perlas-para-los-cerdos')
add('PerryBibleFellowship', '/perry-bible-fellowship')
add('PhilHands', '/phil-hands')
add('PhoebeandHerUnicorn', '/phoebe-and-her-unicorn')
add('Pi', '/pi')
add('Pibgorn', '/pibgorn')
add('PibgornSketches', '/pibgornsketches')
add('Pickles', '/pickles')
add('PicpakDog', '/picpak-dog')
add('PicturesinBoxes', '/pictures-in-boxes')
add('PigtimesCartoon', '/pigtimes-cartoon')
add('Pinkerton', '/pinkerton')
add('PipethePelican', '/pipe-the-pelican')
add('PirateMike', '/pirate-mike')
add('PlanB', '/planb')
add('PlasticBabyHeadsfromOuterSpace', '/plastic-babyheads')
add('Pluggers', '/pluggers')
add('PoliceLimit', '/policelimit')
add('PoochCafe', '/poochcafe')
add('PoorlyDrawnLines', '/poorly-drawn-lines')
add('PopCultureShockTherapy', '/pop-culture-shock-therapy')
add('Poptropica', '/poptropica')
add('PreTeena', '/preteena')
add('PricklyCity', '/pricklycity')
add('Primusthebadphilosopher', '/primus-the-bad-philosopher')
add('Puppets', '/puppets')
add('RabbitsAgainstMagic', '/rabbitsagainstmagic')
add('Rackafracka', '/rackafracka')
add('RaisingDuncan', '/raising-duncan')
add('RandolphItch2am', '/randolphitch')
add('RandomActsofNancy', '/random-acts-of-nancy')
add('RealLifeAdventures', '/reallifeadventures')
add('RealityCheck', '/realitycheck')
add('RebeccaHendin', '/rebecca-hendin')
add('RedMeat', '/redmeat')
add('RedandRover', '/redandrover')
add('RegularCreatures', '/regular-creatures')
add('ReplyAll', '/replyall')
add('ReplyAllLite', '/reply-all-lite')
add('RicigsToonTrivia', '/ricigs-toon-trivia')
add('RipHaywire', '/riphaywire')
add('RipleysBelieveItorNot', '/ripleysbelieveitornot')
add('RipleysBelieveitorNotSpanish', '/espanol/ripleys-en-espanol')
add('Risible', '/risible')
add('RobRogers', '/robrogers')
add('RobbieandBobby', '/robbie-and-bobby')
add('RobertAriail', '/robert-ariail')
add('RonWarren', '/ron-warren')
add('RosaDominical', '/espanol/rosa-dominical')
add('RoseisRose', '/roseisrose')
add('Rosy', '/rosy')
add('Rubes', '/rubes')
add('RudyPark', '/rudypark')
add('SCAIRYTALESTheNotSoScaryFairyTales', '/Scairy-Tales:-the-not-so-scary-fairy-tales!')
add('SOD', '/sod')
add('SandSharkBeach', '/sandshark-beach')
add('SantavsDracula', '/santa-vs-dracula')
add('SarahsScribbles', '/sarahs-scribbles')
add('SavageChickens', '/savage-chickens')
add('ScaryGary', '/scarygary')
add('ScorchedEarth', '/scorched-earth')
add('ScottStantis', '/scottstantis')
add('Scurvyville', '/scurvyville')
add('ShirleyandSonClassics', '/shirley-and-son-classics')
add('Shoe', '/shoe')
add('Shoecabbage', '/shoecabbage')
add('Shortcuts', '/shortcuts')
add('ShutterbugFollies', '/shutterbug-follies')
add('SignGarden', '/signgarden')
add('SigneWilkinson', '/signewilkinson')
add('SincerelyBeatrice', '/sincerely-beatrice')
add('SkinHorse', '/skinhorse')
add('Skippy', '/skippy')
add('Skylarking', '/skylarking')
add('SleepytownBeagles', '/sleepytown-beagles')
add('SmallNerdyCreatures', '/small-nerdy-creatures')
add('Smith', '/smith')
add('SnowSez', '/snowsez')
add('SoccerDude', '/soccer-dude')
add('SoccerEarth', '/soccer-earth')
add('SookyRottweiler', '/sooky-rottweiler')
add('SouptoNutz', '/soup-to-nutz')
add('Spectickles', '/abbotts-spectickles')
add('Speechless', '/speechless')
add('SpeedBump', '/speedbump')
add('SpinCrazy', '/spin-crazy')
add('SportsbyVoort', '/sports-by-voort')
add('SpottheFrog', '/spot-the-frog')
add('StankoAndTibor', '/stankotibor')
add('Starslip', '/starslip')
add('SteveBenson', '/stevebenson')
add('SteveBreen', '/stevebreen')
add('SteveKelley', '/stevekelley')
add('StoneSoup', '/stonesoup')
add('StrangeBrew', '/strangebrew')
add('StuartCarlson', '/stuartcarlson')
add('SubSub', '/subsub')
add('SuburbanFairyTales', '/suburban-fairy-tales')
add('SunnyStreet', '/sunny-street')
add('SunshineState', '/sunshine-state')
add('SuperFunPakComix', '/super-fun-pak-comix')
add('SuperSiblings', '/super-siblings')
add('Sylvia', '/sylvia')
add('TOBY', '/toby')
add('TankMcNamara', '/tankmcnamara')
add('Tarzan', '/tarzan')
add('TarzanenEspaol', '/espanol/tarzan-en-espanol')
add('TeacherInk', '/teacher-ink')
add('TedRall', '/tedrall')
add('TeddyBearsKillingSpree', '/teddy-bears-killing-spree')
add('TenCats', '/ten-cats')
add('ThatMonkeyTune', '/that-monkey-tune')
add('ThatNewCarlSmell', '/that-new-carl-smell')
add('Thatababy', '/thatababy')
add('ThatisPriceless', '/that-is-priceless')
add('ThatsLife', '/thats-life')
add('TheAcademiaWaltz', '/academiawaltz')
add('TheAdventuresofHeromanGuy', '/adventures-of-heroman-guy')
add('TheArgyleSweater', '/theargylesweater')
add('TheAwkwardYeti', '/the-awkward-yeti')
add('TheBarn', '/thebarn')
add('TheBeauforts', '/the-beauforts')
add('TheBellies', '/the-bellies')
add('TheBentPinky', '/the-bent-pinky')
add('TheBigPicture', '/thebigpicture')
add('TheBoobiehatch', '/the-boobiehatch')
add('TheBoondocks', '/boondocks')
add('TheBornLoser', '/the-born-loser')
add('TheBuckets', '/thebuckets')
add('TheCardinal', '/thecardinal')
add('TheCity', '/thecity')
add('TheCreeps', '/the-creeps')
add('TheDailyDrawing', '/the-daily-drawing')
add('TheDinetteSet', '/dinetteset')
add('TheDoozies', '/thedoozies')
add('TheDuplex', '/duplex')
add('TheElderberries', '/theelderberries')
add('TheFamilyBlend', '/the-family-blend')
add('TheFlyingMcCoys', '/theflyingmccoys')
add('TheFuscoBrothers', '/thefuscobrothers')
add('TheGreenMonkeys', '/thegreenmonkeys')
add('TheGrizzwells', '/thegrizzwells')
add('TheHumbleStumble', '/humble-stumble')
add('TheInsolentLemon', '/the-insolent-lemon')
add('TheKChronicles', '/thekchronicles')
add('TheKnightLife', '/theknightlife')
add('TheLeftyBoscoPictureShow', '/leftyboscopictureshow')
add('TheLightedLab', '/the-lighted-lab')
add('TheLostBear', '/the-lost-bear')
add('TheMartianConfederacy', '/the-martian-confederacy')
add('TheMeaningofLila', '/meaningoflila')
add('TheMiddletons', '/themiddletons')
add('TheNorm40', '/the-norm-4-0')
add('TheNormClassics', '/thenorm')
add('TheOldManAndHisDog', '/old-man-and-his-dog')
add('TheOtherCoast', '/theothercoast')
add('TheQuinnAndFinnShow', '/quinn-and-finn')
add('TheQuixoteSyndrome', '/the-quixote-syndrome')
add('TheSmileFile', '/mid-life-with-alan')
add('TheSunshineClub', '/the-sunshine-club')
add('TheUnemployed', '/the-unemployed')
add('TheWanderingMelon', '/the-wandering-melon')
add('TheWinyChild', '/the-winy-child')
add('TheWizardofIdSpanish', '/espanol/wizardofidespanol')
add('TheWorstThingIveEverDone', '/the-worst-thing-ive-ever-done')
add('ThinLines', '/thinlines')
add('Thingsesque', '/thingsesque')
add('Think', '/think')
add('TimEagan', '/tim-eagan')
add('TinyConfessions', '/tiny-confessions')
add('TinySepuku', '/tinysepuku')
add('TnCComics', '/tnc-comics')
add('TodaysDogg', '/todays-dogg')
add('TomToles', '/tomtoles')
add('TomtheDancingBug', '/tomthedancingbug')
add('TooMuchCoffeeMan', '/toomuchcoffeeman')
add('ToughTown', '/tough-town')
add('Trivquiz', '/trivquiz')
add('Trucutu', '/espanol/trucutu')
add('TruthFacts', '/truth-facts')
add('Tutelandia', '/espanol/tutelandia')
add('Twaggies', '/twaggies')
add('TwitchyOToole', '/twitchy-otoole')
add('TwoBits', '/two-bits')
add('USAcres', '/us-acres')
add('UnMannerlyWays', '/mannerly-ways')
add('UncleArtsFunland', '/uncleartsfunland')
add('UnderstandingChaos', '/understanding-chaos')
add('UnstrangePhenomena', '/unstrange-phenomena')
add('UpandOut', '/up-and-out')
add('Vernscartoons', '/vernscartoons')
add('ViewsAfrica', '/viewsafrica')
add('ViewsAmerica', '/viewsamerica')
add('ViewsAsia', '/viewsasia')
add('ViewsBusiness', '/viewsbusiness')
add('ViewsEurope', '/viewseurope')
add('ViewsLatinAmerica', '/viewslatinamerica')
add('ViewsMidEast', '/viewsmideast')
add('ViewsoftheWorld', '/viewsoftheworld')
add('ViiviAndWagner', '/viivi-and-wagner')
add('WTDuck', '/wtduck')
add('WaltHandelsman', '/walthandelsman')
add('WarpedAnddemented', '/warped-and-demented')
add('WatchYourHead', '/watchyourhead')
add('WayOutComics', '/way-out-comics')
add('WaynoVision', '/waynovision')
add('WeePals', '/weepals')
add('WelcometoFriendly', '/welcome-to-friendly')
add('WendlesLife', '/wendleslife')
add('WhiskeyFalls', '/whiskey-falls')
add('WideOpen', '/wide-open')
add('WillSays', '/will-says')
add('WillyWho', '/willy-who')
add('WinLoseDrew', '/drewlitton')
add('WindingRoads', '/winding-roads')
add('Winston', '/winston')
add('WitoftheWorld', '/witoftheworld')
add('WittOfWill', '/witt-of-will')
add('WizardofId', '/wizardofid')
add('WizardofIdClassics', '/wizard-of-id-classics')
add('WorkingDaze', '/working-daze')
add('WorkingItOut', '/workingitout')
add('WorldofWonder', '/world-of-wonder')
add('Wrobbertcartoons', '/wrobbertcartoons')
add('WrongHands', '/wrong-hands')
add('WuMo', '/wumo')
add('WumoenEspaol', '/espanol/wumoespanol')
add('Wyatt', '/wyatt')
add('YennyLopez', '/yenny-lopez')
add('YennyenEspaol', '/espanol/yennyespanol')
add('YouCanwithBeakmanandJax', '/beakman')
add('ZackHill', '/zackhill')
add('ZenPencils', '/zen-pencils')
add('ZeroGravity', '/zero-gravity')
add('Ziggy', '/ziggy')
add('ZiggyenEspaol', '/espanol/ziggyespanol')
add('Zootopia', '/zootopia')
