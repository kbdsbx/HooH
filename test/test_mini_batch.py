import math
from erud.nous import nous
import numpy as np

def load_dataset() :
    train_X = [[-0.21687013460912397   ,  0.8050501531955674    ,
         0.7112745129750352    ,  2.1085556194555104    ,
         0.9074663561826478    , -0.6997544823478554    ,
         0.6347694037487634    ,  1.611480897660506     ,
         0.6804786947885496    ,  0.1192465677966777    ,
         0.687898974876001     , -0.3799941955875272    ,
         1.3823924658337758    ,  0.06322388812108806   ,
         0.3443362791803338    , -0.5403698518517657    ,
         1.5452465100172483    ,  1.2162085595832561    ,
        -0.2819680880359144    ,  0.33781812453034743   ,
         0.28957237615911247   ,  1.2215122870472839    ,
         0.6176706177393292    , -0.8218544768621541    ,
         0.0656270495139235    ,  0.6725132122570536    ,
        -0.017408579990933246  , -0.4897675047106226    ,
         0.9825328071146462    ,  1.1704485102573838    ,
         1.8735303829085932    ,  0.7490828063634427    ,
        -0.29208260357330884   ,  0.7034286555228321    ,
         1.3522126754316033    ,  1.7856304580672169    ,
        -0.059392285017313196  ,  1.248830459625162     ,
         0.14563389930160864   , -0.8745550764910618    ,
        -1.2390771313881677    , -0.7345644028914526    ,
         2.1276802295653203    ,  0.860677104213494     ,
        -0.875243737214038     , -0.58799714269615      ,
         0.5499964072741872    ,  1.4442158181747269    ,
        -1.0451614857582052    ,  1.0594859748294407    ,
         0.24779878153171273   ,  0.4712222142310507    ,
        -0.29024251697220366   ,  0.6107694699681232    ,
         0.25443871865397427   ,  0.44295912038734236   ,
         0.04391412653773297   ,  0.40081941853113656   ,
         0.8934245282211113    , -0.1771598096975539    ,
         0.11390784750811597   ,  0.4884508202088407    ,
         0.846805304950562     , -1.0166324959727775    ,
         0.49406966006367076   ,  0.2865843424412534    ,
         0.4910559294030101    ,  0.6990340879765469    ,
         0.7647039749849919    ,  1.0345136404864648    ,
        -0.1377610463434472    ,  0.9059567566858441    ,
        -0.8295097660058667    ,  0.2055074633560173    ,
        -1.003930108146991     ,  1.5979424302008907    ,
         2.1838810218758526    ,  1.9637623001913624    ,
         1.2428366601630259    ,  0.2713953131940279    ,
         0.4834256490264236    , -0.22137806319285613   ,
        -0.5861536982746407    ,  0.14259536789585658   ,
         1.1216959827210542    ,  0.593933379501729     ,
         1.2734427799096812    ,  2.1668605310274547    ,
        -0.37465368294846263   ,  0.2496176865267065    ,
         1.7309763247547982    ,  0.5484538531533085    ,
        -0.8659156425623559    ,  2.0634550785464443    ,
         0.35497473055302453   ,  0.7485903624713466    ,
         1.0796641521676076    ,  1.8721150491340124    ,
         0.42395394025786237   ,  1.043084686511512     ,
         1.1400189951119004    ,  1.0390709543811225    ,
        -0.12984475403205903   ,  1.9924095532691533    ,
         1.238624269452694     ,  0.13293650194989437   ,
        -0.4568849160425898    ,  1.1422506404706154    ,
         1.4553617090195303    ,  2.1252180120111746    ,
        -0.5980170620409588    ,  1.2374755731177844    ,
         1.333082373523272     , -0.887618833705501     ,
         1.7131051547418081    , -0.9479540307893389    ,
         1.1158821229259197    , -0.6698974886089348    ,
         0.13724492950076353   ,  1.7879252926897804    ,
        -0.7841712682242522    , -1.0193243894855055    ,
         0.2831768610579386    , -0.9935457841258968    ,
         0.848506490003373     ,  1.749983671280786     ,
        -0.6905235529739956    ,  1.6883531803722884    ,
         1.163470144206876     , -0.493354749771154     ,
        -0.16795412356373113   ,  1.6299776484103985    ,
        -0.5627158731728119    ,  0.9768627607557118    ,
         0.23897677061621694   ,  1.9842520502348417    ,
         0.8840442051562318    ,  0.10689518437584582   ,
         0.7402045730669063    ,  0.7153945805425572    ,
         0.9241299853705498    ,  2.0020881627375573    ,
         0.5897127459972076    , -0.6811405802777893    ,
        -0.8442839527163905    , -0.2629441170384757    ,
        -0.2773873150273068    ,  0.2038383548709358    ,
         0.5719663873570848    ,  1.1664082490208505    ,
        -0.3045107337814129    , -0.47741459251998375   ,
        -1.0486257457558381    , -0.8180348346140218    ,
         0.42194018572419245   ,  1.5975675788681802    ,
         2.178928960650894     ,  0.14370937037997317   ,
        -0.6918395591696676    ,  1.4528940455872674    ,
         0.7228372367819702    ,  0.2275590621896371    ,
         1.608431545580764     ,  1.3688802267421438    ,
         0.4679332324656925    ,  0.864959703840583     ,
        -0.034113112471803944  ,  2.1997467361586733    ,
        -0.4889321019100493    , -1.3034170373399978    ,
         1.3109719235602524    ,  2.158492357318477     ,
        -1.110913240134094     , -0.6586770613254792    ,
         0.6452554669058406    ,  0.7829012268481786    ,
         2.0020991197676468    ,  0.3383706780005611    ,
         1.8843034101430651    ,  0.7327439629087722    ,
        -0.4502946041171041    ,  0.5052200035418964    ,
         0.7038321732873525    ,  0.6875732508185238    ,
         0.5493922414412838    , -0.7008930486251154    ,
         0.892249630776649     ,  1.6591839389950462    ,
         0.22452308373986163   , -1.041515231826639     ,
         0.47979229818417773   ,  0.21500810423042732   ,
         1.993635375584489     ,  1.2779704246755292    ,
         0.45948166205539703   ,  1.5529732036762658    ,
         1.8586292348196356    ,  1.0176965752472682    ,
         0.3414385781353886    ,  0.7102256741336118    ,
         0.37747780818921817   , -0.2583011015774409    ,
         0.44919919723198426   , -0.9079586477608478    ,
         1.9791247354931842    ,  0.7426357115434947    ,
         0.3013582508950659    ,  0.5352181942473647    ,
        -0.14656235318702132   ,  0.030347566277692986  ,
         0.6982325123872419    , -1.0449481839508623    ,
         1.9942132011229232    ,  0.5269774996937787    ,
         0.8466473750231918    ,  0.8036923815387998    ,
         0.3549317050608838    ,  1.5293936723463806    ,
         0.752688187233304     ,  1.4409803516261626    ,
         1.6402558204413216    ,  0.6397404870858059    ,
         0.8238908430022658    , -0.7132468291083719    ,
         0.6649366738533323    ,  1.3405513174153492    ,
         1.1832097562366979    , -0.2037282476408331    ,
         0.8446405333842222    ,  0.35518509140992316   ,
         1.8767082311384964    , -0.03639441222793888   ,
         1.9922236282374803    ,  0.09790120959529597   ,
         0.901101619298109     , -0.3654082770736448    ,
         0.5293058309236915    ,  0.13991879890769704   ,
         1.1017803457011377    ,  0.41081864712224536   ,
         1.7301474033561894    ,  0.450112960274645     ,
         0.0679886817726113    , -0.2911995168561249    ,
         1.7402997867488188    , -0.881115192764527     ,
         1.0580841324212131    , -0.0611485608989466    ,
         0.20581324296566694   ,  0.09806524374452008   ,
         1.1504382377332945    ,  1.3699710614306715    ,
         1.3846575798941525    , -0.06861858200954801   ,
        -0.029525990218067913  , -1.302601193682007     ,
         0.6710764651876181    , -0.33810429394791186   ,
         1.190584245719892     , -0.700983811220688     ,
         0.7634339446640476    , -0.7293981428799723    ,
         2.0251261460979904    , -0.16191502731345936   ,
         1.3971415950491584    ,  1.6069922747533858    ,
        -0.03327029261239628   ,  0.16864613606750883   ,
         0.2683326557976421    ,  0.8962720701071476    ,
         0.8345848198359427    ,  0.6075536284224947    ,
         0.4397554189238271    ,  0.2956264044910645    ,
         0.7952452619009376    , -0.23259751451135147   ,
         1.1302603901457322    , -0.08073124985313082   ,
         1.049855080556877     ,  2.0874189120350026    ,
        -0.8328563584755962    , -0.8051615526782454    ,
        -0.5228641948705716    , -0.13487870079984055   ,
        -0.9817648802567397    ,  1.365628148087376     ,
        -0.19929355701574034   ,  0.7790790379029503    ,
        -0.5418848063907443    , -1.0026514595837093    ,
        -0.8682218268666585    , -0.944233966254139     ,
         0.1960188496848712    ,  0.6976232385692607    ,
        -1.1193894937772184    ,  1.8627728350415784    ,
         1.6323822925853761    , -0.8805163732758882    ,
         1.6087991457771322    ,  0.547725598273234     ],
       [ 1.0154493742029873    , -0.5579733951321297    ,
        -0.4100602407591063    ,  0.5208149143227435    ,
         0.45934943086427465   ,  0.18919560283238107   ,
        -0.13899492754080495   , -0.12293165505904963   ,
         0.3567461829204638    , -0.13514376453139398   ,
         0.5400993429655997    ,  0.7487160635802411    ,
        -0.2731355781196349    ,  1.0075360158826647    ,
         0.8975232487248512    ,  0.6009226279301189    ,
        -0.2846014799655063    , -0.3918443434816443    ,
         0.6567675523407877    ,  0.6946512752156029    ,
         1.0686603848760987    , -0.4413815799327181    ,
        -0.1880745146585691    ,  0.44004737323399773   ,
         0.2737096817795547    , -0.6210545263910926    ,
         1.0891151394936371    ,  0.8118009241943493    ,
        -0.446309917123317     ,  0.1462169262485249    ,
        -0.2402783469883779    , -0.25856924049168      ,
         1.176657178712185     ,  0.7495491293268164    ,
        -0.3841826892850636    , -0.15956911375947952   ,
        -0.0351849157741323    , -0.07429291723736997   ,
         0.15226156645118039   ,  0.445815988364272     ,
         0.49712512891583027   ,  0.5501174022293798    ,
         0.1668452022535422    , -0.17913038484103586   ,
         0.4845386934599015    ,  0.378067501665855     ,
         0.6661057197081797    ,  0.10285118055182822   ,
         0.47396999606956786   , -0.7174703291984066    ,
         0.5669323153744155    ,  1.3922899020361368    ,
         1.3076364911107636    , -0.434472669257491     ,
         0.9622192930462687    ,  0.7739962792995377    ,
         0.7340349147768389    ,  0.681964207557109     ,
        -0.11231783821826327   ,  1.3789293917784655    ,
         0.4776792146437262    ,  1.0483937032113047    ,
        -0.2870910395376293    , -0.12594942163574502   ,
        -0.40713637443532436   ,  1.104000794953233     ,
        -0.44425511080799385   ,  0.4679484331621273    ,
         0.458543188591294     ,  0.8186909095646544    ,
         0.9230819793684643    ,  0.24656209458519251   ,
         0.6533348648380393    ,  0.5122661022251643    ,
         0.38529160735448337   , -0.05662983088938743   ,
         0.5972633399747728    ,  0.022580461400002805  ,
        -0.253299857665638     , -0.3605071022471864    ,
         0.5216881379505109    ,  0.07707925993635556   ,
         0.9103173634643265    , -0.3229412792930929    ,
         0.7484037956417844    , -0.3475522019798127    ,
        -0.2919344631170677    ,  0.7167733182605771    ,
         0.7501095729436074    ,  0.21912322201301385   ,
         0.2986754519365061    ,  0.6513307645966909    ,
        -0.1275874567283974    ,  0.29755946797357075   ,
         0.26873814201180307   ,  0.4673032881109059    ,
        -0.4805780901393062    ,  0.13964730364990113   ,
         1.215517472491586     , -0.40890542245795214   ,
        -0.31779836648574283   , -0.32131014284173043   ,
         0.9100329346145932    ,  0.29734857781474505   ,
        -0.5949314104168341    ,  0.6204885012109503    ,
         0.5141280434276813    , -0.5963613960160699    ,
        -0.10259592024231773   ,  0.01134185043673469   ,
         0.49065835366277727   ,  0.038065774487395065  ,
        -0.4695454704832065    ,  0.854794238312327     ,
        -0.29625815247667253   ,  0.5781555760397089    ,
         0.5077469174322399    ,  0.830605986291046     ,
         1.131051413910871     , -0.09295019616197252   ,
         0.43255643211755307   , -0.45103073359656587   ,
        -0.018177717872938204  ,  0.557437105389174     ,
         0.3041727319610236    , -0.00006794680043517576,
         0.7350751963940555    , -0.20950483712943146   ,
         0.3054028793526287    ,  0.9004922980364867    ,
         0.3276980934628092    , -0.6405785438839011    ,
         0.2574025479367376    ,  0.45501264645708095   ,
         0.9216245991460043    ,  0.5305880996122345    ,
         0.11097587213693616   ,  0.09988068042124423   ,
         0.259652761589377     , -0.21565255867078842   ,
        -0.5072284363959626    ,  0.1581682237787275    ,
         1.1337513544503188    ,  0.793125816773135     ,
         0.5699547169364405    ,  1.131352443313655     ,
         0.397401911963789     ,  0.1169334330425561    ,
         0.19391875862510488   , -0.36518089695377853   ,
         1.2595456425067024    ,  0.48877630325802696   ,
         0.7031117700467245    ,  0.1547378566571287    ,
        -0.2090303339368374    ,  0.05909544307284742   ,
         0.4323518298203776    , -0.813421157218514     ,
         0.3852910789862914    , -0.23274427527787048   ,
        -0.44399136326714594   ,  1.1119499465206837    ,
        -0.03302409401036093   , -0.4411902756045692    ,
        -0.169862056824718     , -0.7322806049522748    ,
         1.018480053495379     ,  0.4309903035412297    ,
         0.6950023362553832    , -0.0530664059651097    ,
        -0.1036357391210819    ,  0.38345998525261304   ,
         0.10616629736810526   ,  0.8697012102613115    ,
        -0.5943988232134926    , -0.6802235947327725    ,
         0.10986053440461503   ,  0.0661293293653766    ,
        -0.1805276962451411    , -0.17834151417679583   ,
         0.849388035158636     ,  0.7732275936118651    ,
         0.32601588189650743   , -0.3101809161828974    ,
         0.6516363203226005    ,  0.9434666844210814    ,
         0.6338181295357979    ,  0.5908387844900291    ,
        -0.16756021791462924   ,  0.06366672753017472   ,
         0.297567013469334     ,  1.06753718745909      ,
         0.30389416090745114   , -0.4602152936680648    ,
        -0.30183647050070067   , -0.12306806820378666   ,
        -0.15404402555002758   , -0.6724693503119652    ,
         0.39887004127262493   ,  0.5124529445907602    ,
        -0.501092337679221     ,  0.07535528467035077   ,
         0.13016170134750246   ,  0.40844616017461643   ,
        -0.4167766004152699    ,  0.6003168155459637    ,
        -0.4805399979365349    ,  0.7108894189496994    ,
         1.1464602217799773    ,  0.6645022066078875    ,
         0.1519937822213241    ,  0.683668298102548     ,
         0.051954516689354246  , -0.4020980347503       ,
         0.35547429834313893   ,  1.2364189616429258    ,
        -0.12767456048351405   , -0.4168443765868832    ,
         0.17151969410019594   , -0.481916971891114     ,
         0.17072211152833078   ,  0.7388863951293434    ,
         0.8407084845059972    ,  0.9237597721829157    ,
         1.0622168149420717    , -0.02897935852033301   ,
         0.4467562266866188    ,  0.5781511433892107    ,
        -0.4173860113664079    , -0.24153112429737783   ,
         0.4564987324411714    ,  1.1657510896576988    ,
        -0.14084793584575295   ,  0.2550555398959873    ,
        -0.5819116504309242    ,  1.1499959796058719    ,
         0.6086762257983982    ,  0.7319320278096912    ,
        -0.6463855316728068    ,  1.0606404914914047    ,
        -0.14747014872116548   , -0.37525747481881566   ,
         0.7098205301351413    , -0.1350419689478951    ,
        -0.008057481294605762  ,  0.10271773616885578   ,
        -0.22814834308797832   ,  0.8249544199573712    ,
        -0.10435219912568525   ,  1.2689334065799582    ,
         0.4044759155732531    , -0.4636525390594465    ,
        -0.23156860792267348   ,  0.5402201661267749    ,
         0.9149301577369877    ,  0.4439608155542619    ,
        -0.743782327295289     ,  1.0417366995805202    ,
        -0.48095748073162004   ,  0.6646702180672923    ,
        -0.15080093168059755   ,  1.0937065824858145    ,
         0.08319394237509467   ,  0.05893422983757747   ,
        -0.018909155085687857  , -0.010002609273468854  ,
        -0.19840361553415764   ,  0.20219239052157628   ,
        -0.4538142460817957    , -0.3114075864001573    ,
         1.143757533007461     ,  0.8087320929714383    ,
        -0.03183641400788073   ,  1.0874807613713147    ,
         0.561392793392855     ,  0.2802544095976449    ,
         0.8966219622401985    ,  0.20929293702445914   ,
         0.0963820084929865    ,  0.5514880037826354    ,
         0.9414882625742643    ,  1.0024139058188304    ,
         0.8782483539095688    ,  1.35887716141586      ,
         0.7640836136191096    , -0.11981625670044507   ,
         0.9044153698243971    ,  0.5087654386526267    ,
         0.8106056679538556    ,  0.021193514139368718  ,
         0.30341021281083086   ,  0.3045607510789698    ,
         0.402221985213447     , -0.3033566865086433    ,
         0.5186236528589874    , -0.07268822814213635   ,
        -0.5136323888416846    ,  0.15783028376333053   ,
        -0.6658235507219985    ,  0.3481746137071188    ]]
    train_Y = [[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1,
        1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
        0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1,
        0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1,
        0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0,
        1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1,
        1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1,
        1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1,
        0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]]
    
    return np.array(train_X), np.array(train_Y)


def set_mini_batch(train_X, train_Y) :
    m = 300
    s = 64

    permutation = list(np.random.permutation(m))
    shuffled_X = train_X[:, permutation]
    shuffled_Y = train_Y[:, permutation].reshape((1, m))

    n = math.floor(m/s)
    batches = []

    for k in range(0, n) :
        mX = shuffled_X[:, k*s : (k+1) * s]
        mY = shuffled_Y[:, k*s : (k+1) * s]

        miniB = (mX, mY)
        batches.append(miniB)
    
    if m % s != 0 :
        mX = shuffled_X[:, m - (m % s):]
        mY = shuffled_Y[:, m - (m % s):]

        miniB = (mX, mY)
        batches.append(miniB)

    
    return batches

import erud.upf as upf

def no_test_mini_batch() :
    train_X, train_Y = load_dataset()
    batches = set_mini_batch(train_X, train_Y)

    assert train_X.shape == (2, 300)
    assert train_Y.shape == (1, 300)
    assert len(batches) == 5

    rate = 0.0007
    num_iterations = 10000
    
    g = nous(
        '''
        X:(64, 2) ->

            matmul W1:he((2, 5), 4) add b1:(5) -> relu ->
            matmul W2:he((5, 2), 10) add b2:(2) -> relu ->
            matmul W3:he((2, 1), 4) add b3:(1) -> sigmoid ->

        cross_entropy Y:(64, 1) -> cost -> J:$$
        '''
    ).parse()

    g.setUpdateFunc('W1', upf.norm(rate))
    g.setUpdateFunc('W2', upf.norm(rate))
    g.setUpdateFunc('W3', upf.norm(rate))
    g.setUpdateFunc('b1', upf.norm(rate))
    g.setUpdateFunc('b2', upf.norm(rate))
    g.setUpdateFunc('b3', upf.norm(rate))

    for i in range(num_iterations) :
        for b in batches :
            g.setData('X', b[0].T)
            g.setData('Y', b[1].T)

            g.fprop()
            g.bprop()

        if i % 1000 == 0 :
            print("Cost after iteration {}: {}".format(i, g.getData('J')))
    print("Cost after iteration {}: {}".format(num_iterations, g.getData('J')))



def no_test_mini_batch_with_momentum() :
    train_X, train_Y = load_dataset()
    batches = set_mini_batch(train_X, train_Y)

    assert train_X.shape == (2, 300)
    assert train_Y.shape == (1, 300)
    assert len(batches) == 5

    rate = 0.0007
    beta = 0.9
    num_iterations = 10000
    
    g = nous(
        '''
        X ->

            matmul W1:he((2, 5), 4) add b1:(5) -> relu ->
            matmul W2:he((5, 2), 10) add b2:(2) -> relu ->
            matmul W3:he((2, 1), 4) add b3:(1) -> sigmoid ->

        cross_entropy Y -> cost -> J:$$
        '''
    ).parse()

    g.setUpdateFunc('W1', upf.momentum(rate, beta))
    g.setUpdateFunc('W2', upf.momentum(rate, beta))
    g.setUpdateFunc('W3', upf.momentum(rate, beta))
    g.setUpdateFunc('b1', upf.momentum(rate, beta))
    g.setUpdateFunc('b2', upf.momentum(rate, beta))
    g.setUpdateFunc('b3', upf.momentum(rate, beta))

    for i in range(num_iterations) :
        for b in batches :
            g.setData('X', b[0].T)
            g.setData('Y', b[1].T)

            g.fprop()
            g.bprop()

        if i % 1000 == 0 :
            print("Cost after iteration {}: {}".format(i, g.getData('J')))
    print("Cost after iteration {}: {}".format(num_iterations, g.getData('J')))



def test_mini_batch_with_adam () :
    train_X, train_Y = load_dataset()
    batches = set_mini_batch(train_X, train_Y)

    assert train_X.shape == (2, 300)
    assert train_Y.shape == (1, 300)
    assert len(batches) == 5

    rate = 0.0007
    beta1 = 0.9
    beta2 = 0.999
    num_iterations = 10000
    
    g = nous(
        '''
        X ->

            matmul W1:he((2, 5), 4) add b1:(5) -> relu ->
            matmul W2:he((5, 2), 10) add b2:(2) -> relu ->
            matmul W3:he((2, 1), 4) add b3:(1) -> sigmoid ->

        cross_entropy Y -> cost -> J:$$
        '''
    ).parse()

    g.setUpdateFunc('W1', upf.adam(rate, beta1, beta2))
    g.setUpdateFunc('W2', upf.adam(rate, beta1, beta2))
    g.setUpdateFunc('W3', upf.adam(rate, beta1, beta2))
    g.setUpdateFunc('b1', upf.adam(rate, beta1, beta2))
    g.setUpdateFunc('b2', upf.adam(rate, beta1, beta2))
    g.setUpdateFunc('b3', upf.adam(rate, beta1, beta2))

    for i in range(num_iterations) :
        for b in batches :
            g.setData('X', b[0].T)
            g.setData('Y', b[1].T)

            g.fprop()
            g.bprop()

        if i % 1000 == 0 :
            print("Cost after iteration {}: {}".format(i, g.getData('J')))
    print("Cost after iteration {}: {}".format(num_iterations, g.getData('J')))


