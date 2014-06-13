<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1402365018249" ID="ID_1333860051" MODIFIED="1402512824353" STYLE="bubble" TEXT="iteration over JSON">
<edge STYLE="sharp_bezier"/>
<font BOLD="true" NAME="SansSerif" SIZE="12"/>
<node CREATED="1402365091244" ID="ID_62748362" MODIFIED="1402365094504" POSITION="right" TEXT="on arrays">
<node CREATED="1402365099439" ID="ID_573438389" MODIFIED="1402365115701" TEXT="of plain elements">
<node CREATED="1402365146047" ID="ID_1436819489" MODIFIED="1402365415389" TEXT="Reimplement xargs -n option">
<icon BUILTIN="button_ok"/>
</node>
</node>
<node CREATED="1402365117271" ID="ID_531284097" MODIFIED="1402365125677" TEXT="of plain elements and subarrays">
<node CREATED="1402365178686" ID="ID_250015753" MODIFIED="1402365190981" TEXT="recursion control">
<node CREATED="1402365191735" ID="ID_1004152268" MODIFIED="1402365196885" TEXT="algorithm">
<node CREATED="1402365197479" ID="ID_46312951" MODIFIED="1402365426163" TEXT="depth">
<icon BUILTIN="button_ok"/>
</node>
<node CREATED="1402365199198" ID="ID_1116444298" MODIFIED="1402365426163" TEXT="width">
<icon BUILTIN="button_ok"/>
</node>
</node>
<node CREATED="1402365205703" ID="ID_619643371" MODIFIED="1402365216813" TEXT="limiting recursion depth">
<node CREATED="1402365217391" ID="ID_281403622" MODIFIED="1402365480882" TEXT="What to do with the rest?">
<icon BUILTIN="help"/>
<node CREATED="1402365487335" ID="ID_1498667693" MODIFIED="1402365506173" TEXT="Add option to skip or stop on unacceptble elements"/>
</node>
</node>
</node>
<node CREATED="1402365227463" ID="ID_1479051781" MODIFIED="1402365244109" TEXT="pass subarray as list of arguments">
<node CREATED="1402365253655" ID="ID_30482935" MODIFIED="1402365559117" TEXT="set level of recursion, all subarrays lower than it will be threated as big subarray"/>
</node>
</node>
<node CREATED="1402365128335" ID="ID_691204325" MODIFIED="1402365139725" TEXT="of objects">
<node CREATED="1402365273231" ID="ID_1432644863" MODIFIED="1402365700067" TEXT="allow to name keys and values in command line">
<node CREATED="1402365287558" ID="ID_462677284" MODIFIED="1402365577029" TEXT="One object per execution"/>
</node>
<node CREATED="1402365315239" ID="ID_1730409802" MODIFIED="1402365586922" TEXT="nested arrays/objects?">
<icon BUILTIN="help"/>
</node>
</node>
<node CREATED="1402365140663" ID="ID_458615968" MODIFIED="1402365144556" TEXT="mixed">
<node CREATED="1402365336383" ID="ID_382151034" MODIFIED="1402365339845" TEXT="jpath?"/>
<node CREATED="1402365372055" ID="ID_1237564442" MODIFIED="1402365386954" TEXT="ignore non-fitted?"/>
</node>
</node>
<node CREATED="1402365595551" ID="ID_369974976" MODIFIED="1402365745329" POSITION="right" TEXT="on objects">
<node CREATED="1402365611319" ID="ID_244656449" MODIFIED="1402365617861" TEXT="of plain elements">
<node CREATED="1402365618447" ID="ID_854971923" MODIFIED="1402365647724" TEXT="Allow specify keys and values positions">
<node CREATED="1402365648358" ID="ID_631786553" MODIFIED="1402365663643" TEXT="pairs are unordered">
<icon BUILTIN="messagebox_warning"/>
</node>
</node>
<node CREATED="1402365668263" ID="ID_557357341" MODIFIED="1402365700067" TEXT="Allow use values by key name">
<arrowlink DESTINATION="ID_1432644863" ENDARROW="Default" ENDINCLINATION="-124;33;" ID="Arrow_ID_309572047" STARTARROW="None" STARTINCLINATION="-164;49;"/>
</node>
</node>
<node CREATED="1402365708799" ID="ID_1470283087" MODIFIED="1402365774661" TEXT="of arrays">
<node CREATED="1402365714951" ID="ID_1184626445" MODIFIED="1402365727171" TEXT="of plain elements">
<node CREATED="1402365727734" ID="ID_1219997233" MODIFIED="1402365760613" TEXT="special syntax for arrays"/>
</node>
<node CREATED="1402365777007" ID="ID_320916582" MODIFIED="1402365781301" TEXT="of arrays">
<node CREATED="1402365781879" ID="ID_174982974" MODIFIED="1402365787525" TEXT="same as for normal list">
<node CREATED="1402365788055" ID="ID_193549935" MODIFIED="1402365793292" TEXT="recursion and so on"/>
</node>
</node>
<node CREATED="1402365796991" ID="ID_404687671" MODIFIED="1402365813485" TEXT="of objects">
<node CREATED="1402365813999" ID="ID_1241770879" MODIFIED="1402365822637" TEXT="allow foo[bar[baz]] like syntax"/>
</node>
<node CREATED="1402365826231" ID="ID_1756842060" MODIFIED="1402365830980" TEXT="of mixed elements">
<node CREATED="1402365831615" ID="ID_1010766361" MODIFIED="1402365839810" TEXT="forbid/ignore?">
<icon BUILTIN="help"/>
</node>
</node>
</node>
</node>
<node CREATED="1402511861252" ID="ID_1883473209" MODIFIED="1402512335599" POSITION="left" TEXT="try#2">
<node CREATED="1402511866484" ID="ID_1491862435" MODIFIED="1402511947455" TEXT="default recursion level = 1:&#xa;[ {non:recursion}, ..., {} ] &#xa;iterate only over array">
<node CREATED="1402511950252" ID="ID_1003024419" MODIFIED="1402512033751" TEXT="Can be changed - R 3:&#xa;[ [ [ &#xa;     [&apos;non&apos;, &apos;iterable&apos;]&#xa;] ] ]&#xa;&#xa;-R 0:&#xa;&#xa;{&apos;use&apos;:&apos;me&apos;}"/>
</node>
<node CREATED="1402512057188" ID="ID_1892542960" MODIFIED="1402513070425" TEXT="No recursion over objects&#xa;or iteration over pairs">
<node CREATED="1402512082996" ID="ID_626557358" MODIFIED="1402512096586" TEXT="If yes, create seprare program">
<node CREATED="1402512098284" ID="ID_1695652255" MODIFIED="1402512104450" TEXT="Or add separate syntax"/>
</node>
</node>
<node CREATED="1402512107124" ID="ID_524329252" MODIFIED="1402512149418" TEXT="At the recursion depth iteration starts">
<node CREATED="1402512157796" ID="ID_570046451" MODIFIED="1402512173361" TEXT="Can be array or single element"/>
<node CREATED="1402512175676" ID="ID_794407067" MODIFIED="1402512189170" TEXT="All deeper elements can be called only by jpath"/>
</node>
<node CREATED="1402512879245" ID="ID_856898812" MODIFIED="1402512899547" TEXT="If some objects found on levels higher than interation depth, warn and stop">
<node CREATED="1402512900221" ID="ID_620555230" MODIFIED="1402512938169" TEXT="But allow to process single elements&#xa;like they was on recursion depth level">
<node CREATED="1402512938717" ID="ID_526348733" MODIFIED="1402512943195" TEXT="Is this viable case?">
<node CREATED="1402512943813" ID="ID_1581992168" MODIFIED="1402512986377" TEXT="[1, [{&apos;foo&apos;:2, &apos;bar:3}] ]"/>
<node CREATED="1402512991605" ID="ID_1238052665" MODIFIED="1402513010743" TEXT="Will think later, do not implement yet"/>
</node>
</node>
</node>
<node CREATED="1402512190356" ID="ID_1150589691" MODIFIED="1402512250744" TEXT="If we need to &apos;jpath-strip&apos; some &#xa;pieces before recursion,&#xa;it can be done before calling &#xa;iterator (in pipe)"/>
<node CREATED="1402512256812" ID="ID_992816332" MODIFIED="1402513037076" TEXT="normal elements of objects just called by names">
<node CREATED="1402512276476" ID="ID_559276889" MODIFIED="1402512313624" TEXT="foo[&apos;bar&apos;]&#xa;OR&#xa;foo.bar&#xa;FOR&#xa;{&apos;foo&apos;:{&apos;bar&apos;:&apos;value&apos;}}"/>
</node>
<node CREATED="1402512316796" ID="ID_333503793" MODIFIED="1402512333018" TEXT="arrays can be additionally iterated">
<node CREATED="1402512343853" ID="ID_1543790643" MODIFIED="1402512378440" TEXT="normally, by substituting &#xa;all arrays values as arguments">
<node CREATED="1402512379309" ID="ID_1528371664" MODIFIED="1402512467832" TEXT="echo &quot;[{&apos;a&apos;:[1,2]}, {&apos;a&apos;:[3,4]}&quot; | iterator mycommand ${.a}&#xa;&#xa;will call:&#xa;mycommand 1 2&#xa;mycommand 3 4"/>
</node>
<node CREATED="1402512477669" ID="ID_594323305" MODIFIED="1402512485451" TEXT="but it can be limited">
<node CREATED="1402512487181" ID="ID_1034581870" MODIFIED="1402512692504" TEXT="echo &quot;[{&apos;a&apos;:[1,2,3]}, {&apos;a&apos;:[4,5,6]}&quot; | iterator mycommand ${.a}&#xa;&#xa;limit 2:&#xa;mycommand 1 2&#xa;mycommand 3 &#xa;mycommand 4 5&#xa;mycommand 6&#xa;&#xa;limit 1:&#xa;mycommand 1&#xa;mycommand 2&#xa;mycommand 3&#xa;mycommand 4">
<node CREATED="1402512592909" ID="ID_500654825" MODIFIED="1402512621427" TEXT="Unfitted arrays can be trimmed">
<node CREATED="1402512641925" ID="ID_654087420" MODIFIED="1402512665424" TEXT="Limit 1, trim&#xa;echo &quot;[{&apos;a&apos;:[1,2,3]}, {&apos;a&apos;:[4,5,6]}&quot; | iterator mycommand ${.a}&#xa;&#xa;mycommand 1&#xa;mycommand 4"/>
</node>
<node CREATED="1402512718293" ID="ID_158912704" MODIFIED="1402512736956" TEXT="Check if jpath has different notation for &apos;all array&apos;">
<node CREATED="1402512737581" ID="ID_814499059" MODIFIED="1402512756755" TEXT="If there is natural slices, forget about trimming"/>
</node>
</node>
</node>
<node CREATED="1402512549293" ID="ID_1435169006" MODIFIED="1402512568600" TEXT="joinification (from different objects)&#xa;is not planned">
<node CREATED="1402512569213" ID="ID_195380193" MODIFIED="1402512573507" TEXT="can&apos;t see valid cases"/>
</node>
</node>
<node CREATED="1402513080133" ID="ID_494467149" MODIFIED="1402513104569" TEXT="How to handle mix of simple values and objects?&#xa;[ 1, {&apos;foo&apos;:&apos;bar&apos;} ]">
<node CREATED="1402513105493" ID="ID_1373479769" MODIFIED="1402513108603" TEXT="check jpath">
<node CREATED="1402513625198" ID="ID_1616269249" MODIFIED="1402513643689" TEXT="jpath says &apos;&apos; (empty string) is query for simple elements"/>
<node CREATED="1402513644693" ID="ID_1081471936" MODIFIED="1402513676785" TEXT="We gonna use some sign (let says &apos;$&apos; for initial). ${} meants element itself"/>
</node>
<node CREATED="1402513695078" ID="ID_1626924870" MODIFIED="1402513743771" TEXT="Means we can&apos;t mix different types in same level&#xa;(except int/str)">
<node CREATED="1402513737054" ID="ID_472028185" MODIFIED="1402513799252" TEXT="Or allow dicts &apos;as is&apos;">
<node CREATED="1402513745542" ID="ID_841636560" MODIFIED="1402513808538" TEXT="&gt;&gt;&gt; for a in [ 1, {&apos;a&apos;:&apos;b&apos;} ]:&#xa;...     jpath.get(&apos;&apos;,a)&#xa;... &#xa;1&#xa;{&apos;a&apos;: &apos;b&apos;}&#xa;"/>
</node>
<node CREATED="1402513838326" ID="ID_1086865447" MODIFIED="1402514124330" TEXT="Will depends on error control (see)">
<arrowlink DESTINATION="ID_1394217147" ENDARROW="Default" ENDINCLINATION="-83;-120;" ID="Arrow_ID_58679661" STARTARROW="None" STARTINCLINATION="-383;7;"/>
</node>
</node>
</node>
<node CREATED="1402515744952" ID="ID_1900278602" MODIFIED="1402515748150" TEXT="operators?">
<node CREATED="1402515748736" ID="ID_1276555104" MODIFIED="1402515750366" TEXT="Later"/>
</node>
<node CREATED="1402513849102" ID="ID_1394217147" MODIFIED="1402514124330" TEXT="Error control">
<node CREATED="1402513873814" ID="ID_771644849" MODIFIED="1402514633362" TEXT="invalid object during recursion:&#xa;&#xa;Recursion depth 2:&#xa;[ [3,4], 1,  [5, 6] ] | iterate mycommand -R 2 ${}">
<node CREATED="1402514251014" ID="ID_1149483767" MODIFIED="1402514261660" TEXT="stop at load">
<node CREATED="1402514268895" ID="ID_1798117312" MODIFIED="1402514334564" TEXT="Stderr: invalid object for recursion &apos;1&apos;, will not processing anything"/>
</node>
<node CREATED="1402513907126" ID="ID_1953831149" MODIFIED="1402514255733" TEXT="Stop at error">
<node CREATED="1402514169670" ID="ID_797539573" MODIFIED="1402514523826" TEXT="mycommand 3 4&#xa;Stderr: invalid object for recursion &apos;1&apos;, aborting"/>
</node>
<node CREATED="1402513910958" ID="ID_1749773334" MODIFIED="1402513912996" TEXT="ignore">
<node CREATED="1402514169670" ID="ID_415512024" MODIFIED="1402514527698" TEXT="mycommand 3 4&#xa;Stderr: invalid object for recursion &apos;1&apos;, ignored&#xa;mycommand 5 6">
<node CREATED="1402514217342" ID="ID_1835333694" MODIFIED="1402514222117" TEXT="warning can be supressed"/>
</node>
</node>
</node>
<node CREATED="1402513917798" ID="ID_124541087" MODIFIED="1402514491738" TEXT="Invalid object during query:&#xa;&#xa;echo &quot;[{&apos;foo&apos;:&apos;bar&apos;},1, {&apos;foo&apos;:&apos;baz&apos;}] | iterate mycommand FOO ${.foo}">
<node CREATED="1402514290006" ID="ID_1360244343" MODIFIED="1402514292453" TEXT="stop at load">
<node CREATED="1402514268895" ID="ID_289720697" MODIFIED="1402514406556" TEXT="Stderr: Not an object: &apos;1&apos;, will not processing anything"/>
</node>
<node CREATED="1402513935022" ID="ID_1528448087" MODIFIED="1402513940980" TEXT="stop">
<node CREATED="1402514366903" ID="ID_12383902" MODIFIED="1402514583194" TEXT="mycommand FOO bar&#xa;Stderr: Not an object: &apos;1&apos;, aborting "/>
</node>
<node CREATED="1402513942926" ID="ID_300935327" MODIFIED="1402513958588" TEXT="Skip bad entry (do not call command)">
<node CREATED="1402514169670" ID="ID_1049998650" MODIFIED="1402514588738" TEXT="mycommand FOO bar&#xa;Stderr: Not an object &apos;1&apos;, ignored&#xa;mycommand FOO baz">
<node CREATED="1402514217342" ID="ID_1793828056" MODIFIED="1402514222117" TEXT="warning can be supressed"/>
</node>
</node>
<node CREATED="1402513964278" ID="ID_275796982" MODIFIED="1402513971972" TEXT="substitute nothing">
<node CREATED="1402514169670" ID="ID_610378467" MODIFIED="1402514599818" TEXT="mycommand FOO bar&#xa;mycommand FOO&#xa;mycommand FOO baz"/>
</node>
</node>
</node>
<node CREATED="1402515122983" ID="ID_679339942" MODIFIED="1402515125246" TEXT="Format">
<node CREATED="1402515125959" ID="ID_427184504" MODIFIED="1402515128214" TEXT="jpath"/>
<node CREATED="1402515129263" ID="ID_309102084" MODIFIED="1402515140654" TEXT="&apos;Special symbols&apos;">
<node CREATED="1402515141239" ID="ID_502349308" MODIFIED="1402515144814" TEXT="{} seems fine">
<node CREATED="1402515146615" ID="ID_1045408094" MODIFIED="1402515182462" TEXT="interator mycommand argument {.foo} {.bar[3]} {.baz.foo.bar[4.foo]}"/>
</node>
</node>
</node>
</node>
</node>
</map>
