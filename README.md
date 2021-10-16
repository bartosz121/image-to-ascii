# Image to ASCII Converter

Simple tool which converts image to ASCII written in Python

![Demo gif](./demo.gif)

## How it works

- Load image using Pillow
- Resize image to given dimension (default 100x40)
- Convert to grayscale
- Assign proper character to each pixel based on its grayscale value
- Save output to file

## Run Locally

Clone the project

```bash
  git clone https://github.com/bartosz121/image-to-ascii
```

Go to the project directory

```bash
  cd image-to-ascii
```

Create new virtual environment

```bash
  python -m venv env
```

Activate environment

```bash
  # on Linux
  source env/bin/activate

  # on Windows
  ./env/Scripts/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Try it out!

```bash
  python image_to_ascii/i2a.py <path_to_image>
```

Open output.txt file to see the result!

## Usage

- --help

```bash
$ python image_2_ascii/i2a.py --help
Usage: i2a.py [OPTIONS] IMAGE

  Image to ASCII convertion

  By default uses those chars (black --> white)
  $@B%8&WM#*oahkbdpqwmZO0QLCUYXzcvunxrjft/\()1}{[]?-_+~<>i!lI;:,^.

Arguments:
  IMAGE  Path to image  [required]

Options:
  --output-size <INTEGER INTEGER>...
                                  Set custom output width and height
                                  [default: 100, 40]
  --output-filename TEXT          Set name of the txt file where output will
                                  be saved  [default: output]
  -r, --reverse                   Reverse the order of chars used in
                                  convertion
  --no-resize                     Output width and height are the same as the
                                  image
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

- --output-size

```bash
python image_2_ascii/i2a.py image_2_ascii/image.png --output-size 50 40
# ASCII size set to (50, 40)
```

- --output-filename

```bash
python image_2_ascii/i2a.py image_2_ascii/image.png --output-filename ascii
# Output saved to ascii.txt!
```

- Set custom filename, reverse characters and do not resize

```bash
python image_2_ascii/i2a.py image_2_ascii/image.png -r --no-resize --output-filename ascii-reversed
```

## TODO

- [ ] Let user specify their own set of characters for convertion
- [ ] Maintain aspect ratio instead of resizing to hard coded value
- [ ] Colored convertion

## Examples

```
......................................,;li<~+++____+++~<>!l:^.......................................
...................................:i~_------______________+~<!:....................................
.................................,<-?------____________+++++++++>:..................................
................................^+?--+l:,;<__________++++++++++++~;.................................
................................;----:.....~_______+++++++++++++~+<.................................
................................;----;....^~______++++++++++++~~~~~^................................
................................:--___iII!+_____++++++++++++~~~~~~<^................................
................................:--___----_____++++++++++++~~~~~~~<^................................
................................:__++++++++++++++~+++++++~~~~~~~~~<^................................
.................................^^^^^^^^^^^^^^^^,~++++~~~~~~~~~~~<^................................
.....................^;l!iiiiii!!!!!!!!!!!!!!!!!!!~+++~~~~~~~~~~~~<^.1unnnnnr\?I....................
...................I~_------------_____________+++++~~~~~~~~~~~~~~<^.tLCCCCCCCCX/l..................
.................:~?-----_____________++++++++++++~~~~~~~~~~~~~~~~<^./CUUUUUUUUUCz_.................
................;_-----_____________++++++++++++~~~~~~~~~~~~~~~<<<<^./CUUUUUUUYYYUY+................
...............,_-----____________+++++++++++++~~~~~~~~~~~~~~~<<<<>^./CUUUUUYYYYYYUc;...............
...............>----_____________++++++++++++~~~~~~~~~~~~~~~<<<<<<i..fCUUUYYYYYYYYYC}...............
..............^_--_____________++++++++++++~~~~~~~~~~~~~~~<<<<<<<<:.:zUUYYYYYYYYYYYYu^..............
..............I--____________+++++++++++++~~~~~~~~~~~~~~~<<<<<<<>:..)CYYYYYYYYYYYYYYX!..............
..............I-___________+++++++++++++++++++~~~~~~~~~~~~<<<>!;..^}UUYYYYYYYYYYYYXXY+..............
..............I-__________+++++++++~>!I;;;:::::::::::::::::,^...:_xCUYYYYYYYYYYYXXXXU]..............
..............I-________+++++++++>;...,l<+--________________-])jcCUYYYYYYYYYYYYXXXXXU]..............
..............I-______++++++++++I..:]jzCLLLLLLLLLLLCCCCCCCCCCCCCUYYYYYYYYYYYYXXXXXXXY+..............
..............I-_____++++++++++I..-zQLLCCCCCCUUUUUUUUUUUUUUUUUYYYYYYYYYYYYYXXXXXXXXXXl..............
..............,____+++++++++++>..?LLCCCCCCCUUUUUUUUUUUUUUUUUYYYYYYYYYYYYYXXXXXXXXXXYn^..............
...............>_+++++++++++++l.,zLCCCCCCUUUUUUUUUUUUUUUUUYYYYYYYYYYYYYXXXXXXXXXXXXY[...............
...............:_+++++++++++~+I.iCCCCCCCUUUUUUUUUUUUUUUUYYYYYYYYYYYYYYXXXXXXXXXXXXYx,...............
................!_+++++++++~~+I.>CCCCCUUUUUUUUUUUUUUUUYYYYYYYYYYYYYYXXXXXXXXXXXXXYul................
.................!+++++++~~~~+I.>CCCUUUUUUUUUUUUUUUUUYYYYYYYYYYYYYXXXXXXXXXXXXXYYfI.................
..................;>++++++++~+I.>CCUUUUUUUUUUUUUUUCCCCCUUUUUUUUUUUUUUUUYYYYYYYcf+...................
....................:li><<<>><;.>CUUUUUUUUUUUUUUUz((((((((((((((((((((((((()[~I.....................
................................>CUUUUUUUUUUUUUUUn,^^^^^^^^^^^^^^^^.................................
................................>CUUUUUUUUUUUUYYYYcccccccccccvvvvvn:................................
................................>CUUUUUUUUUUYYYYYYYYYYYYYUUUUUYYXYc;................................
................................>UUUUUUUUUYYYYYYYYYYYYYXYu1?{jXXXXc;................................
................................>UUUUUUUYYYYYYYYYYYYYYXYj,....}YXXc;................................
................................lYUUUUUYYYYYYYYYYYYYXXXU\.....+YXXc;................................
.................................1CUUYYYYYYYYYYYYYXXXXXXX1i;l?vXXYf^................................
..................................?vCCUYYYYYYYYYXXXXXXXXXYXczYYYX/;.................................
...................................,_/vXUUUYYYYXXXXXXXXXXYYYXcr1i...................................
......................................,i-1/ruczXXXXXXzcuxf([~I^.....................................

```

```
{{[]?--_++~~<<>ii!!!llII;;:::,,,,^^^^..........................^^^^,,,,:::;;IIIll!!ii>><~~++_--?][[{
[]??-__+~~<>>ii!!llII;;:::,,,^^^....................................^^^,,,:::;;IIll!!ii>><~~+__-??][
]?-__++~<>>ii!!lII;;;::,,^^^............................................^^^,,:::;;IIl!!ii>><~~+__-?]
?-_++~<<>ii!!lII;;::,,,^^...^^.............................................^^^,,::;;IIll!ii><<~++_-?
-_+~~<>>i!!lII;;::,,^^......lpL(!.............................................^^,,::;;IIll!ii><<~+__
++~<<>i!!llI;;::,,^^.........X$@W0{:............................................^^,,::;;Ill!!i>><~++
~~<>>i!llI;;::,,^^...........;h@B$m[-;............................................^^,,::;;Ill!ii><~~
<<>ii!lII;::,,^^..............-&B@r<-)],............................................^^,,::;IIl!!i><<
>>i!!lI;;::,,^.................(BB\<~~]1<....................................^l]rUm+..^^,,:;;Ill!i>>
ii!llI;;:,,^^...................r@\<~~~~}[,...............................^i-fM@$$O^...^^,,::;IIl!ii
i!lII;::,^^......................uj<~~~~<?)l............................;_{[+[&B@kI......^^,::;IIl!!
!lII;::,^^........................[{<~~~~<+)<.........................!]}?~<<?W$o<........^^,,:;IIl!
lII;::,^^..........................?1~~~~~~~)~......................l{1_~~~~<{Ba<...........^,,:;IIl
II;:,,^.............................~\-<~~~~<)~..,li<<>il:^.......,]1-~~~~~~<jq!.............^,,:;II
I;:,,^..............^l^..............l(}~~~~~~(-]{}{[]][{}}[_;...>)?~~~~~~~~[):...............^,,:;I
;:,,^^.............,{{{?!^............^?/]~~~~?]+~<<~~~~<<~_]1[i]1+~~~~~~~-1+..................^,,:;
::,^^.............^}-<~_{}_;............I}(?_~~~~~~~~~~~~~~~<~_)1<~~~~~~-}];....................^,::
:,^^.............^{?<~~~~~?}[i^...........lf?~~~~~~~~~~~~~~~~~~<~~~<<+]1[l......................^^,:
,,^..............]]~~~~~~~~~_{1_:.........I}~~~~~~~~~~~~~~~~~~~~~~}}(1_;.........................^^,
,^..............+{<~~~~~~~~~~<~]1[!.......]-~~<+_<~~~~~~~~~~~~~~~<\)I.............................^,
^^.............!1~~~~~~~~~~~~~~~~-}[!....^(~~+Ydx)~~~~~~~~~~~<<<~~-]..............................^^
^.............,)+~~~~~~~~~~~~~~~~~<+[{<^.l)<<v$m^c\<~~~~~~~~<[(]<~+1...............................^
^.............[?~~~~~~~~~~~~~~~~~~~~~+[}>_{<<U$8b8/<~~~~~~~<n)]*r<~)...............................^
.............<}<~~~~~~~~~~~~~~~~~~<+~~<~]r+<<?q88C~~~~++~~~_#ct%o+~}................................
............,)~~~~~~~~~~~~~~~~~~<_)f/t~<_(1f\_~{]<<~~<{}<~~~p$$$w~+[................................
............]?<<<~~~~~~~~+++++++-j}-_{)~)YLCLU]<<~]-_[(-><<<]LdL?<_{................................
............[{[{{[[[{}}111))))))r)<~~~}fCQYYYCx<~<(hko#bv/1~<<<><~~{................................
.............^;>-}\tft\()))(()))t)<~~~<_v0YYYLr<~<}ohkkoMMj<~~~\zzx(................................
...................:>-1/fft\()))(j~~~~~~<\LCLz-~~<?mmmmmpp_<~<\QUULC,...............................
........................;>?1/ff/(j{<~~~~~<)c)+~~~~+XcvcYZf<~~<vUYYUX^...............................
.............................;<]1tx~~~~~~~<[1<~~~~<fnrjxn~~~~<fQUUQ[................................
.................................^](<~~~~~~<}}<~~~<]cxuu-<~~~~+fXQ1.................................
.................................:tx-~~~~~~~<(]~~~~<}rt_<~~~~~<_1<..................................
................................^\\\f~~~~~~~~+(+~~~~<~<~~~~~<_({:...................................
................................1t))t\<~~~~~~~_+~+-+~~~~~~~+[1}]....................................
...............................]j))))n1~~~~~~~~~~~[)}{[?~~~+_~<1,...................................
..............................+r))))x~>{~~~~~~~~~~~?}{?+~~~~~~<{>...................................
^............................lu\))))//[?f_~~~~~~~~~~~~~~~]-~~~~?-..................................^
^............................:?\ft()))\rcx}+~~~~~~~~~~~~+(~~~~~_[..................................^
^^..............................I-(f/()j1}[~~~~~~~~~~~~<}{<~~~~+1..................................^
,^.................................:\f)j~~~~~~~~~~~~~~~<(+~~~~~+).................................^,
,,^................................_zjt\<~~~~~~~~~~~~~~+(~~~~~~_)................................^,,
:,^^..............................+qdOz?~~~<~~~~~~~~~~~?)<~~~~~]]................................^,,
::,^.............................+pbbdn~~<+]-~~~~~~~~~~[}<~~~~<)-...............................^,,:
;:,,^............................~Xdkk/<+}nzn\{+~~~~~~<[{<~~~~~/1{,![;.........................^,,:;
;;:,^^.............................~vw?~--\f\(]\-~~~~~<]}<~~~~{}<-//z}........................^^,:;;
II;:,,^..............................\+~~<)1)(?+}+~~~~<{(<<<<+\+<-/tU].......................^^,:;;I
lI;;:,,^............................^(~~~~11()\<~+~~~~~+)\}[]\]<+/1tvI......................^^,:;;Il
!lI;;:,,^...........................^(~~~<[j))r-<~~~~~~~<_[}}}+<)\)\/......................^,,:;;Il!
!!lI;;:,,^...........................1+~<~1u))jf-++-[}}}[?_~<<<-/))j!.....................^,,:;;Il!!
ii!lII;::,^^.........................+(+-1)u\)\n)))((((((((1{]?}))/}....................^^,::;IIl!!i
>ii!llI;;:,,^.........................1f())jr)(u)))))))))))((((()(f:...................^,,::;IIl!ii>
<>>i!llI;;::,^^........................?tt\\v()u\/tfft/\\(()))f((ji..................^^,::;;Il!!i>><
~<<>i!!lII;;:,,^^.......................,~{)rx(u}-~~<<+]})\//tv/f>.................^^,,:;;IIl!!i><<~
+~~<>ii!!lII;;:,,^^.........................._t~..........^,,,_};................^^,,::;IIll!ii><<~+
_++~<<>ii!llII;::,,^^..........................................................^,,,::;;Ill!ii><<~++_
--_+~~<>>i!!llII;::,,^^^....................................................^^,,:::;IIIl!!i>><~~+__-
??-__+~<<>ii!!llII;;::,,^^^..............................................^^^,,::;;IIll!!ii><<~++_-??
]]?--_++~<<>>i!!llII;;;::,,,^^^......................................^^^,,,:::;;IIll!!i>><<~++_--?][
{[]]?-__++~<<>iii!!llII;;:::,,,,^^^..............................^^^^,,,:::;;IIIll!ii>><<~~+__-??][{
```

```
vcvvuuunuvvvvvcvcvuvzcvuvuuvnvvvvvvvvvcvvcccvzvvcvvvzvcvccccccvuuuuvnvunuuuunvvvvcvcvvcccvcvccvvvuun
uvvccvvuvcczuvvvvvuzccccvcuvvvcccvuvvvccccccuuxrrrffjffjrxxuuvvuvcvcuuunnunuuunuuuucvvcvvvcvuvvvvnnn
vnvvvvuuuvvvvcvcccvcvvzzcvuvcczXzczXcurt()}[]--+_-_+~-++++<+_?]{1\tjruuuvuunuvuvuuvcvvvvcccczcccunvu
zvvcvcvvvccccccccccvvzzzcccccXXzvn/}]]?]-??++_-+_+_++_++_+~~~~<<<<<<~-[(fnvuuuuvvvccvccczzzccvzccuvu
XXzvcXzzzXzzcvzzXXcczzXzXcXcccx1]-+_-]{})){???--+++~~+<<~<ii><~~++~~>>>!!>-)ruvvvcvvvccczccccvvvvvuu
XXXzzXYUXXXXXzXXYXXzXzzXXYcj/]?-?[{{{1)/\1[[[[]]?--_--+++~<>ii!i!!>~+++>>!I;l~{xvzczccczXcXXzcczcvcc
XzXzUYYYXYYXXXYXYXYYXzXzvf)[[{}}111}}(tf\){}}}{[[[[[[-___+~~<<>i!llIll!><>ill;;I~(vzvcccXczzzXzczzzc
zYYXUYXXXUYXXYYXXXYYXXct{][{1111())))/f/(/}1}}}{}[]?]?-___+~~~<>ii!illlIIl!ll!l;:;<(vzzzzXzXXYYXXcXX
XUUYUYUYYYYXYYYYUYCUUx{??{{{1}1)((/trunxft\\((1}}{[]?----__+~~>>ii!!i!llIIII!!ilI;::</czzYUYYXzzYzXz
YUYXUYUYYUUUUCUUUUCXf[?][{1(tjnvcYUCLUCQLCYYzzzvuxxf(}[]-_++~+<<>>ii>!llllllIIlll;II,I+xzUYczzzXzXYX
XYXUCYYUUCCCUCYUUYz1]?]1tnzYLC00OOOZZZZOOOQQCLUXXXzcnxt\}[]?__+~~>>!illllIliIII;;;;II;^l1zYXXzXXXXYU
UCYUCCLLCLLCUUYYYu}?-[/nczXUQOZmmqqpqwqpwwwmZZ00LUCYzvxj/(1{[?_+~<<>i!!lllllIl!llI;I;I;:,+xXXXXUUYXY
CCUCCCLLCQLCCUXXx[]-[\nXULOZqbppqbdddppbddpqwqZZOO0LCYvuxf\\1}[-+~~<ii!lI;II;IlIIlII;;;I;,<jXXYUXUYX
UCCUCCQLUCCUCYz/_~<?/uXCQOqwpbqpdpbdbdpbdbpdppwmm00QQCYXvxft\}{]-++~<>i!!lI;II;I;;III;,;I:I!rYYYYUUz
UCCLCCQQLLCCUu)i<>+)rvYU0ZqwqpdpbqdpdddddpdppqqqwZOZ0LUYvnjt/)1}[-_+~>>i!>i!lII;;II;I;I:II:,lxXYzYLX
CCCLLQQQLCLYn/1<<>?\ncYCQZwqppqqpqppwpdpddppqwwwZZOQLUYXcuxjf\\11[?-~<<>i>i!lllIIlI;;:I;:;;:;>zXzUYc
LUUQQQLQ0Lvjrj}i><](rXUCQ0wqwmqwqZmwmwqpqwwwmwwZ00LCUYXzzvurrft/)}{[-++>>!llI;lIIIII:;:;,:;:;,1Xcunx
LLQ00Q00Crxj{?_><+1tnzUQ0OwwZOmqwZwwmmmwwwqmmmm00QCCUUXXXcuunnrjtt\)1{?<illllIIIlII;I;;::::;:;l\jrrt
0L000OOCjxj?+-_<>_/nvzCQQOZZZmmqmqqqwqmmwqwZwwmOZ0QLUCUCUYYXzcvunrrt\}?_>!I!ii!l;llIl;;:;;,;;l^+jffr
ZO0000Onrr[~_-<i!?fvXXCL000Z0mZmwwqwwwqqwwwmmwZZOO0OQQQ0CYUYYUXzcuxj/1]_~>llllIlII;;!l;:;I::I;,lttf(
mZmZ00Yxx/~<_-<<!-juXCQ0OmZZZZZwmwmmwwwwwwmwZO0QQLQQQLQLLCYYXYzvvnxf/}?_~>i!llIIII;:;llI;II:;;;:)/(/
ZmqO0Oxjff_<<-<~i-fvUULOLQLCCLQOZmZZmmmpwZLUzvuncvcXXXXXXXzcvunrrft\({]_<i!!i!IlIII;:ll!IIl:;l;:?j)}
O0O0QXtf()[~<i_~<+\vXYYzcuxxrjxvCOZOO0O0LXxt\\(/\/fjft////t//((())))1{]-~i!il!lllllI;llIl;l;Iil:~/[]
QQLUYv)/([{?-_-_~-1((((/xrnuxnjffnQ0QQQUcj)}{{1tnucccurf\}]-??--?[1)1}[?+<!i!!illIlII;III;l;;!lII}}]
QCUYXc})}?]__~?-~_)}[[1/tj([?]}/jjnLZOQYr1\}1/fnnun}]-?[[}}]]?][1trrf\1[_+i!!!i!!!III;;IIlIIIIllI?)1
UYYYzzn1]+~+_~~+~+jcx\fnYLc((//txXuQpw0Xf)/\xvzLZOZcttjffjftrucXYYYvxt({?+>!l!>i!!II:IIIllllI;llI~)[
nuLXXUt[-++-~>><>]uXUvYUCCUXunxzYYYOqw0zjtfjxcUYCCUCYYXvuxnvXULLQCXcnt({-~illli!l!II;I;IlIll!;IlI>\{
)fYcu/((?~~+<>iii[YU00OQQCUccXUQOQL0Zm0XxjxnuYLQLLUUCYUUCC0000QLLYzux/1?_>ill!ll!!III;I;lIIl!!lII;[]
{1ur(/)){~i<<<!i![zQ0OZmmmwmmwmmOQ0OZwQXzvvcXC0mqpwdpdddwqwZOQCUXcuxt({-~il!Il!lIl!Il:!I;;lll!>I;:?{
{}r})\}\}->>>!ii!-uYCCQOZmmqmwwZ00OwqmLYXczXYU0mqwwqwdpmwmmZQCYXvvrf\}?+>illilI!l!!l!I!l;IIll!!i;,_}
}}/?{}[1?+++<<<i!<\zCC0ZZwmmwmOZ0ZZpqmLYzzcXUUOOZZwmmqqmOZZ0CYzvnrt\)[-~>i!liil!!i>l!l>I!IlIlili!:<j
[{]_{?-+-++<+~+~!![nYQOZZZmZmZZ0QOOwmZCUXcvczUQ000ZOZwZOO00CUXvnjt\)1?+<ii!llll!!!l!iIilI;IIII!ll!I{
?]~-____+~>~~<iiil_tvUQ00OZZZZQCLOZpwOLYccvvnz000O00ZZ0QLLCYcvxj/\)}]-+>i!>!!!l>l!i>!l!II;lI;;!!li;<
[-_++~<~~~~_<>l!!!<1rvXLQOO0QQCczOqwm0XuxxnnjfQmOZ0OZ0QQUYXcnxjt()1}[_~<>!!li!i!Ii!!!!l;lllll;IiI>ii
]_?~+~_~<<>~iil<>!l-\juXUCCLLQOLnnXYvf([??[[]1YZZmO0QLCUYzvnrjt\)}{[?_~<>!!!!lllIi!i!lllIiIIl;;iIl><
?]?<+__~<+!l!<>iiii>}/jnvzzYL0ZmqZXr1[[]?[{}\rXQQLCUUYXXzvnxjf/\\1}[-_~<>!l!l!l!!il!lllllllll;Iill<~
][-+<<<>+~>>>>iii<>!-\jnnuvcXC0OZmw0vtt/\fjnvzzzzvuuczzzcvurfft\\)1[?+~>ii!!l!lil!!il!!il;!lIIIlili<
?[{-+<+>~<>~~~~~i>>ii{ruucccvnrvYYCUUYcxjjjjjft\)/xuzXXzzcuxrf/(()}]?+<>i!!lI!i!ll!!lll!l;IIII;I!I><
[]]?+-_<++~~+~~<i<<<l~(rvzXYXunvXvuccnjft/\))((/rvXzUUYXXvuxrt(()1[]_<~>ii!l!!il!i>llllil;IlI;!i!I<<
{[{?-]-_<+~_+>!!><<i!!<}rczXUC0mw0QQQCUUzvurrrvcXzzXYXXzvnxj/\11}{?-+~<>i!i!iIli>!ii!!!lIl;I;Iliil>>
11)_]]-?_+<~~<i!i>iii!!i?(jucXY0LCCznftftffrrxxnnnuvvvvnrjf\)}1[[[-_+~<>!!!!il>i!ll!!l!IlI;I;I!i!li<
11(-__-?_~>iiii!!ii><!i!i>-)tuzUCCOO0LCCUXXzzXunnnnuunrft\)}}[]-]]-_~<>!!!!!!l!!l!lllIIIlI;I;Il!lli<
/\t1?[[]?_~<iiii<iii<>>i>!!>+{fcUQZwwwqwwOQYYzvuuunxrf/(1}[[]]??-]_~<>!i!!il!!il!!lll!lIllIIII!!i!>~
(\t(??{?-_+~i~<<+<>~>+i!i!<iii~]fzLOOZZm0QUzzvvnjjt\)1}}[??-?]]]-++>>ilii!iill!!ll!>lIl;!lIII!l!l!i<
1)\/]_{_<+_~<~>>>>>~~<i!i!>ii>ii~[fuzCYXzcunxrf()}[[[[[]]?]]?__+<<<<>>!ii!l!Ill!lIl!!i>l!lI;l!!i!Ili
fjjrt_]_+~_~_i>!i>li>!!lI!!!!!ii><+-{1\()(11}}{{{]][??]?[-_+~<<~>+~++~<<i!iil!li!l!!lii!IlIIl;liilli
frjff}~__~~>~<ii>llii!!l;;l!l!!>!<<>~<____--???-_??-__+~~+<<+<+++~-_++~><<<>>!!l!l!lil!IIlI;;lI!!Il!
fjjjtj--?-<!>i>!ii<>i!i!!lIl!i!!!>!>>>>+]??---_+__-++++~~++~++--_+]__-?_--_+<iil!!lI!lI;I!I;I!l!!lIl
tfftt/(---~i<i~iii>i!ii>>>i!li>>ii>i<<<_\f\(11}{[[]-?-?----???]]??}[{{{{[[?_~<>!!il!llIlI!lIlll!i!Il
fftf\\/1{+<<<>>>~+>>i><i!illi>>>>>><><~+turjf/\/()1}]]?]]]?[{[{{}1(()))}{{]-_<<ii!i>!IIIl!lIlI!!ill!

```

```
;;;;;:::;:;::::::::;:::::::::;:;::::::;::::::::::;;::::;Il!!!!lII;;;;;;;;;;;II;;II;;;;;;;;;;;;;;IIII
;;;;;:;;:::::::::::::::::::::;::::::::;;::::;:;;;:;!+}\tjxxxrt(1{[]?-~i!lIIIIIII;;;;;;;II;IIIIIIII;I
;;;;;;;;;:;;:::::::::::;:;;;:::::;:::::::::;;;;:I-tvzvnucvrxvYLOOZZCYYvj\[<lIIIII;;;IIIIIIIIIII;;;;;
I;;;;;;;;;;;;;;;;;;;;::;;;::;;;;;;;;;;:::::;:;I_/rnrt(xu)?}UqhoaaoahhkdqYnf)?<iIIII;;;I;;IIIIII;;I;;
I;;I;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:I!<_[\zYYLOZmw0UzcvuUmqbkbbkbbhwYvrt}]_ilIIII;III;;;;;;;;;;
IIIII;;;;;;;;;;;;;;;;;;;;;;;;;;;;;IIIl<[tvCZphhbhooobZLQLCC0Z0CUYU0wmZZZmZLx)[?-_~iIIII;;;;;;;;;;;;;
;IIIII;;;;;;;;;;;;;;::::;:;:;Il!<+?[})fvcXUYUYzzUmhakdbkqOUczUCQLYvj\(tzLLCYj]~>i><<!lII;I;;;;;;;;;;
;IIIIII;;;;;;;;;;;;;;;;:;l<_}/ruzYYYXzzcvunnxnxf/11(fnzZh##aQcvzczXUzrtfruUQYr(]_>!!i!!III;;;;;;;;;;
;IIIIIII;;;;;;;;;;;;;;>]tcYCQLCLCCYXzzzzczXYXXzvunt)}{{})fv0wpQLXXznnvujfjffrXYuj)?~!ll!lIIIIIII;;II
;III;;;;;;;;;;;;;;;I>)vL0QLQQQQQCLCYCYzzzczXXvuvvvuxf/(1}[{{)jzLQULCXx/tf/fj)[\f\}-]-ilIlI;IIII;;;;I
;IIII;;;;;;;;;IIIl-/zQLLQLLQQQ0QQO0LCXzzvvcXvvvuunnnnxrt\\)}[?{{(fuzYCc\{11)f\+-1c{>~~>!lll;;;;;;;;;
;;;;;;;;;;;;IIII>tUOOOOLLLLQLQQQLQ0LUYYXvuuvuuvvvnxxxxxrjjf/t{]]--?1fnzYr[[-?[]+_cc?i>>i!llI;;;;;;;;
;;;;;;;;;;;IIIi}uUCQ0000000LL0QLCUUUXXzzcvnnxuvcuxnurrxxxnnxn{_?]+~>>_{fur11-><~~jL(<>>i!!lI;;;;I;II
;;;;;;;;;;;Il[cLLCCCQQQQQLQLQQQLLCCXzXzzzzcvvuuvvnnxrrjfrnxxxr1-__+~<>i>-(/)1{+><\0\{<>iiillI;;;;III
III;;;;;;Ill(UCUCLQQLLLQQCCCCXXCUYYXzXzzvvvcXzuvunnxcrxxrrxxttt)]_++~<>>ii~?{1{+>x0zr?ii~_!II;I;;;;;
IIIIIII;;l![CLUYUYUUCLLLCQCCUYXCCLz\/txnuuuvccccunrxxrrxrjfj(?+_+__+++~<<<>i<?]?_UQZc}i>~]]i;;;;;;;;
IIIIIIIIIl[ULYzvzXXXXYUCUQLCYYXYYUu111/ffjxuvuvccuuu\{1tjjjf{<>><~~+_~~~~~<>>>~_-UQZX)>><?{-;I;I;;;;
IIIIIII;I>jrfnYCOmmZZ0LCCYczzXXXc/(\)}}})(\ft))fuvzj_?]?](f(->>>>i>>~~<<~<>><<i>~vLQz\~>i-}[>lI;:;;;
IIIIIIIll>?jQdhhhaaohkdqw0Uzuvvvurttttf([?-[{}}11\uj>i>>ii~~<<<>i!i>><<<>><i>><>>xQYz(<<i+1{]i!I;;;;
lIIII;I!!~vbhkhhhhhahhkbdpqm0Czurfjt/tczt?++~___-]{)+>i!iii><<<<<>>>i><~<<<>>>>ii\0zU{<>i>}{{+!lII;;
IIIIIIIl<udhkkhhhkhhhbpppqqqpwZQXn/1{{\nz{<><~++++~-+~~>iii><<~~~+~<<<>>><<~>>i!l?OXU}+<>i?([?!lIlI;
IIIIIl!~uqdhahhhaahkbbpqwwwwqwmOOQYnt}?-[_~<i!i><<>><~~<iii!<<~~<<<>><>>iiii>>ii!~Xz01~+<i_1{-!IllII
IIIIIl!(ZmZOmbhaaahkdpqpqqqmmwmZO0QLUcr(?+<~>i!!ll!iii>ii<>lli<<<<><<<><<>>ii>>i!!uLw1_+<><{)+i!llII
III;l!!{zUYUXUZhahkdqOOOQLCUCQ0OO0QLCYcnj\]_<<<<i!l;IIll!ii>l!!!!i!><<<<<~~<>>>i!i[Yw1}->>>[t}>!III;
IIIIl!!<-/vXunuZkkpmOYcvvvunuccYCCLLLUXvnj)?_<<~<>>i!lll!iiiil!lll!!li<>~~<><<>il!_Yb(\]>>>{rx-llI;;
lIIIl!!i?Ubr}>-nbadOUujrnnrxvXYCYzzULUXcnt}?_~>>>i>~<i!!iiiii!llll!!!i>>><>i<>illl>Xb(x1<>i-jn1!ii!I
lIIIll!!/daf_<_(qadLujfrrrvC0OCn((1(fuvnf)]-__+<>ii<<<>>>>!!!!i>!!ll!i>><<<><>!llI!cbfcf~>i-\xt<><il
IIIIl!l}QCCLYccCbopzjttjzcvq#&orlI>++-{))]?----_~<>i><<<<>i!!!!i>!l!iii>>>>ii!!lIIIjpuuu+>i+((r]i<!l
IlII!!iUop0QLCZpaa0xjftrY0Oqdbm1_~-_<+?][]]?]]?-+~~~>ii<~~>i!!!!iiiii!!!!ii!ll!lIII}qYjz?~i>)(\\<<il
Illlll<mohbqdbbkapzxjtfxCOOOQLCXxt([?{/xnxjt/1]?-_+~~<>ii<<>iiiiiii>i!!!!!!!lIlI;Il]ZQtQU[ii]f{1-<>l
IIIllI?qbddbbbbbqCurftfxUZZO0LCYvxjjxcXYUXcxj([-___+++~~<>><>iii!!ii><>!!!!!llII;l!-QmjCm/ii~j([_>~~
IIIllI?wddddkbdwUuj/\/trXOZZOOOOO0QQ0QCUYzuj/)]+~~+_++~+~~<<>>><<>iiiii!!!!!!lII;l!~UZnuwr<<>/f-+i~+
IIIIlI~OddddbbwUur/)))\jXQOZZOZZZOZOQLUXcnj/)[_+~~++_+++~<<<>>i><<<>>!!lIIllllIIll!ivQzfbu+~>)v]+i~-
IIIIIl!cbddbbqCxf/)}{{}\YOOZmZOZOZZQLUYcnj/)]_++++++__+++~<<<>ili<<<<i!!lIIIIIIl!!!!x0Yjbz_~>[Uf<>i_
IIIIIll}pkbbwXf()1{}1}[?/LOOOO0OQ0LCYzvxrt)]-+++________++~~>!i><<<<>illl;;IIIllll!l/QLjqC-+>?CU?<!>
IIIIIll>LkkhqX(-++-][?---r0ZZ00QLLCYcnrft({?_+++_-_______~<<<+__~<>>!III;IIIlllIIIll1QCxOL]_<-Cdf<ii
IIIIIIl!fdkkhadCt?-??]}})nL00QQCCUXzurjt/1]?-____---____+++++_-+>>ilI;IIIIIIIII;;Ill{QXnLO{_~-0hZ]>i
IIIIIIll~LbbddkhZxtffxvzXzUQQCCUXzcuxjt/1{]?------_--_++~~____~>!lIIIII;IIIIIIIIIIll{b0Zq0)-+-Oaax>>
IIIIllll!}wpYvUQXrjrrxuvccXYCYXzcvnrjt\)}[]]????-?----_+<>>i>>!lIII;;IIIII;IIIIIIIll\hdahO(]_+Yhaq?>
IIIIllII!!jpLf{[{((\)\/fjxxnzzvvnxjf/(1}{[[[[[[]]]???-_+<>>>>i!llIIIIIIIIIII;;IIIIll\aqhkm/}?~vhhhx>
IIIIIIIlllinpYjt})\t([[??[/fruvunjt/()1}{{{{}}}{{{{[]-_+~~~_+>>ilIIIIIIII;II;;;IIIll{bmbppr(}+\kkhO_
;IIIIIIIll!<XOYQQCU/(11{{\uvccvuxf/())1}{{}}}11111}{]---+_CQ{+~>!lIIIIIIIIIIII;;IIll_dbkpku/\-{qqbk\
;IIIIIIIIl!l-ZmLXvj(1111)tjnuvunjt/)(()111}1)\\(11}{?++__[qbf_<ii!IIIIIIIIIIl!!!lll!<qkbObcnx?]QddoU
IIIIIIIIIIllljaadw0Ynjt\\/tjrnnrt/\\(((((((\\\\\){?-__----_?}{?_+iIIIIIl!!!!!>>>i!!!!QZwvwvzC]-vkpod
;IIIIIIlIIlIl>chhdpwOUcnrt/tffftt/\\\\\\\//\()1[?_+--??--__](}]_<<_][}1))((\/({???_~!uQ0umYvm/](wdok
;;;;IIIIIIIIIIi/LZww0Uzurt\\\\\\/\\(\\\\\(1}[]]???-----_+++_?1)/jucXYXzccccvnrt}[[]->)YLuZUnmm/?zdaa
;;;;IIIIIIIIIII;!_}juuurt\())1{[[{11{[[[[[[{{[[]][[{((\rvU0mpa#aaoahbwXunrtt/()[_+~<>{OQcCLr0px_\wka
;;;;IIIIIIIIIIII;;;;li<~~<<>ilII;!}vurt\()111(jcLmdkMMW8%%8%88MkwZXx({-+~<>>>>>>>>>>i[qOOvwnXmC?[Cdh
;;;II;IIIIIIIIII;;;;;;;;;;;;;;III;!\CLCXvnvUwa&BB%888%%8&#bmQcj([+>i!iii>>iiii>>>>>ii~YUwuq0xUQ)-rmk
;;III;;;;IIIIII;III;IIIIIIIIIIIIIIIl)zQ0qk#MW&%888%8*qCvf}-+<>>i<<i!iiiiiiiiiiiiiii!!lxzZnOpcxXf?1Cq
```
