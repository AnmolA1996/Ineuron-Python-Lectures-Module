#!/usr/bin/env python
# coding: utf-8
string bvariable / String manipulation

        its a combination of character = string 
        so everytime system will try to create indexes inside a string so based on the indexes i'll be able to extract everything. always try to use square bracker []. 

indexes may be both forward or backward 
ex:- s[0,1,2,3,4....] and s[....,-3,-2,-1] (negative indexes)
# In[2]:


s = "ineuron"


# In[3]:


type(s)


# In[4]:


s[0]


# In[5]:


s[5]


# In[6]:


s[-1]

In string i can use double course & as well as single course. 
" " & '' both
# In[7]:


s1n= 'sudh'


# In[8]:


s1n


# In[9]:


s1n[-2]


# In[10]:


s1n[-1]


# In[11]:


'this is my very first programming language's'

here the issue is system is confused where string ends. 


# In[13]:


s2 = "this is my very first programming class's"


# In[14]:


s2


# In[15]:


s2[8]


# In[16]:


s2[1:5]

this time we are not trying to extract single character from the string but we are trying to extracting in between indexes multiple. But it wil exclude the upper bound 5 from [1:5]. It will always starts from 1 go till 5 but it will exclude 5
# In[17]:


s2[6:30]

here you can see data extraction. but we can use one more method in which i can extract characters from the string using jump/skip method 
# In[18]:


s2[6:30:2]


# In[19]:


s = "sudhanshu"


# In[20]:


s


# In[21]:


s[0]


# In[22]:


s[0:9:2]


# In[23]:


s[0:9:1]


# In[24]:


s[0:8:-1]

it means starts from zero go till eight and jump with -1
S U D H A N S H U 
0 1 2 3 4 5 6 7 8
------------------> this is the direction that i have defined so jump into a 
negative direction

how it is creating jump into negative direction so it is creating contradiction in the statement that 
is why its showing blank ''. 
# In[25]:


s[8:0:-1]

it means start from EIGHT GO TILL zero 
S U D H A N S H U 
0 1 2 3 4 5 6 7 8
<-----------------
so here we mentioned try to jump into begative direction
therefore,  there is no contradiction at all. 
s[8:0:-1]

this time it will starts from 8 but upper bound will reach till 1 because upper bound is 0
so it starts from 8 go till zero but excluding zero in a reverse jump with -1. 
# In[27]:


s[8:0:-2]


# In[26]:


s[:-3]

here, what it means it doesn't specified upper or lower bound only,
it is saying that it starts from -3 in a reverse direction. 

S U D H A N S H U
0 1 2 3 4 5 6 7 8
-9-8-7-6-5-4-3-2-1

s[8:0:-2]
in below extract i did not menntioned any upper bound so this will go till last character o a string. 
# In[28]:


s[::1]


# In[29]:


s[0:50:1]


# In[30]:


s[::-1]

Here you can see it is trying to reverse the string only.
# In[31]:


s2


# s2[::-1]

# In[32]:


s2[::-1]


# In[33]:


s[8:0:-1]


# In[34]:


s


# In[35]:


s3 = 'ineuron'


# In[36]:


s3[::-1]


# In[37]:


s3[-2:-7:1]


# In[38]:


s3[-7:-2:1]

0 1 2 3 4 5 6
I N E U R O N
-7-6-5-4-3-2-1
->---------> IT GOES LIKE THIS 
but it will exclude upper bound & it will go till jump 1 
s3[-7:-2:1]
# In[39]:


s[5:0]

by default if you' won't mentioned jump direction it will consider +1 .
s[5:0]
here you can see
S U D H A N S H U
0 1 2 3 4 5 6 7 8
-9-8-7-6-5-4-3-2-1

it means it is starts from to 0 exluding zero by default jump direction 
is positive  so it contradicts & showing blank
# In[40]:


s3[-7:0:1]

----------------------------------------
-7-6-5-4-3-2-1 0 1 2 3 4 5 6 7
--------------->
and jump must be starts into positive direction 
# In[42]:


s[:-1:-1]


# In[43]:


s


# In[44]:


s + 1

we can convert anything into different data type 
if you want to perform concatenation operation it can perform f
# In[45]:


s + '1'


# In[46]:


s + str(1)


# In[47]:


"sudh" + 66666666666666


# In[48]:


"sudh" + "666666666666"


# In[49]:


s


# In[50]:


len(s)


# In[51]:


s *2 

muletiplication with string can be done because it simply means,
it is going to repeat itself.
# In[53]:


s.count('s')


# In[54]:


s.count('sum')

Function of s.count is to confirm how many times string chsracter or
character combination is repeating in string
# In[55]:


s.split('u')


# In[56]:


type(s.split('u'))

split function is basically saying that u is working in this string, 
as splitter or seprator of a data inside a string, 
# In[58]:


sw = "chrome-extension://mhffmephdchhhbfjmdpoaldedhhdanbn/homePage.html"


# In[59]:


sw


# In[61]:


sw.split('m')


# In[63]:


swe = """The samsung group or simply samsung, stylized,as samsung"""

triple quotes can be used for multy line comment now if i am going to execute multiline comment 
with split or string function with seprator it will execute 

# In[64]:


swe.split(' ')

from above data set of a string we can perform multiple operation with the elp of python to replace or 
manipulation with data set that we'll discuss later. 
# In[65]:


sf = """The Samsung Group[3] (or simply Samsung, stylized as SΛMSUNG) (Korean: 삼성 [samsʌŋ]) is a South Korean multinational manufacturing conglomerate headquartered in Samsung Town, Seoul, South Korea.[1] It comprises numerous affiliated businesses,[1] most of them united under the Samsung brand, and is the largest South Korean chaebol (business conglomerate). As of 2020, Samsung has the 8th highest global brand value.[4]

Samsung was founded by Lee Byung-chul in 1938 as a trading company. Over the next three decades, the group diversified into areas including food processing, textiles, insurance, securities, and retail. Samsung entered the electronics industry in the late 1960s and the construction and shipbuilding industries in the mid-1970s; these areas would drive its subsequent growth. Following Lee's death in 1987, Samsung was separated into five business groups – Samsung Group, Shinsegae Group, CJ Group and Hansol Group, and Joongang Group.

Notable Samsung industrial affiliates include Samsung Electronics (the world's largest information technology company, consumer electronics maker and chipmaker measured by 2017 revenues),[5][6] Samsung Heavy Industries (the world's 2nd largest shipbuilder measured by 2010 revenues),[7] and Samsung Engineering and Samsung C&T Corporation (respectively the world's 13th and 36th largest construction companies).[8] Other notable subsidiaries include Samsung Life Insurance (the world's 14th largest life insurance company),[9] Samsung Everland (operator of Everland Resort, the oldest theme park in South Korea)[10] and Cheil Worldwide (the world's 15th largest advertising agency, as measured by 2012 revenues).[11][12]

"""


# In[66]:


sf


# In[68]:


sf.split(' ')


# In[69]:


sf.upper()

here you can see upper function can transform all data set into 
caps letter 

similarly lower function can convert data set into lower caps. 
# In[70]:


sf.lower()

sw = sw.upper()

so here you can see symbol 'sw' is assigning data to sw.upper__
# In[72]:


s = 'sudhanshu'


# In[74]:


s


# In[75]:


s.title()

so here s.title() fuction is transforming only first character into caps 
    similar thing can be done through s.capitalize() function 
# In[77]:


s.capitalize()


# In[78]:


s = 'sudhanshu kumar'


# In[79]:


s


# In[80]:


s.capitalize()

Signature: s.capitalize()
Docstring:
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.
Type:      builtin_function_or_method
# In[81]:


s.swapcase()

Signature: s.swapcase()
Docstring: Convert uppercase characters to lowercase and lowercase characters to uppercase.
Type:      builtin_function_or_method
# In[82]:


s = 'Sudhanshu KumAR'


# In[83]:


s


# In[84]:


''.join(reversed(s))


# In[85]:


s[::-1]


# In[86]:


s=" su dh "


# In[87]:


s


# In[88]:


s.strip()

Signature: s.strip(chars=None, /)
Docstring:
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method
# In[89]:


s.lstrip()


# In[90]:


s.rstrip()

l and r in abkve strips define space in the string
# In[92]:


"a" . join("sudhanshu")


# In[93]:


s


# In[94]:


s = 'sudh'


# In[95]:


s


# In[96]:


s.center(20 , '#')

'########sudh########'
​
​
​
​
​
​
​
Signature: s.center(width, fillchar=' ', /)
Docstring:
Return a centered string of length width.

Padding is done using the specified fill character (default is a space).
Type:      builtin_function_or_method
# In[97]:


s.isupper()

Signature: s.isupper()
Docstring:
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.
Type:      builtin_function_or_method
# In[98]:


s1 = "SUDH"


# In[99]:


s1


# In[100]:


s1.isupper()


# In[101]:


s.islower()


# In[102]:


s1.islower()


# In[103]:


s.isspace()

it means it is asking does this string contain space that is false
Signature: s.isspace()
Docstring:
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.
Type:      builtin_function_or_method
# In[105]:


s = 'Sudhanshu'


# In[106]:


s


# In[107]:


s5 ="56565"


# In[108]:


s5


# In[109]:


s.isdigit()


# In[110]:


s5.isdigit()


# In[111]:


s6 = "sdssd54848"


# In[112]:


s6


# In[113]:


s.isalnum()

it is true because it is showing result based on OR gate 
because alphabet is there and condition satisfied
# In[114]:


s.isalpha()


# In[115]:


s.isalnum()


# In[116]:


s.isnumeric()


# In[117]:


s


# In[118]:


s.startswith('i')


# In[119]:


s.startswith('s')

above condition is false because pythong is case sensitive language
# In[120]:


s.startswith('S')


# In[121]:


s.endswith('n')


# In[122]:


s.endswith('u')


# In[123]:


s6


# In[124]:


s.isdigit()

Signature: s.isdigit()
Docstring:
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.
Type:      builtin_function_or_method
# In[125]:


s.isnumeric()

Signature: s.isnumeric()
Docstring:
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.
Type:      builtin_function_or_method
# In[126]:


s.isascii()


Signature: s.isascii()
Docstring:
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.
Type:      builtin_function_or_methodASCII Chart
Decimal	Binary	Octal	Hexadecimal	Symbol	Description
0	0	0	0	NUL	Null char
1	1	1	1	SOH	Start of Heading
2	10	2	2	STX	Start of Text
3	11	3	3	ETX	End of Text
4	100	4	4	EOT	End of Transmission
5	101	5	5	ENQ	Enquiry
6	110	6	6	ACK	Acknowledgement
7	111	7	7	BEL	Bell
8	1000	10	8	BS	Back Space
9	1001	11	9	HT	Horizontal Tab
10	1010	12	0A	LF	Line Feed
11	1011	13	0B	VT	Vertical Tab
12	1100	14	0C	FF	Form Feed
13	1101	15	0D	CR	Carriage Return
14	1110	16	0E	SO	Shift Out / X-On
15	1111	17	0F	SI	Shift In / X-Off
16	10000	20	10	DLE	Data Line Escape
17	10001	21	11	DC1	Device Control 1 (oft.XON)
18	10010	22	12	DC2	Device Control 2
19	10011	23	13	DC3	Device Control 3 (oft.XOFF)
20	10100	24	14	DC4	Device Control 4
21	10101	25	15	NAK	Negative Acknowledgement
22	10110	26	16	SYN	Synchronous Idle
23	10111	27	17	ETB	End of Transmit Block
24	11000	30	18	CAN	Cancel
25	11001	31	19	EM	End of Medium
26	11010	32	1A	SUB	Substitute
27	11011	33	1B	ESC	Escape
28	11100	34	1C	FS	File Separator
29	11101	35	1D	GS	Group Separator
30	11110	36	1E	RS	Record Separator
31	11111	37	1F	US	Unit Separator
32	100000	40	20	SPACE	Space
33	100001	41	21	!	Exclamation mark
34	100010	42	22	“	Double quotes (or speech marks)
35	100011	43	23	#	Number
36	100100	44	24	$	Dollar
37	100101	45	25	%	Percent
38	100110	46	26	&	Ampersand
39	100111	47	27	‘	Single quote
40	101000	50	28	(	Open parenthesis (or open bracket)
41	101001	51	29	)	Close parenthesis (orclose bracket)
42	101010	52	2A	*	Asterisk
43	101011	53	2B	+	Plus
44	101100	54	2C	,	Comma
45	101101	55	2D	-	Hyphen
46	101110	56	2E	.	Period, dot or full stop
47	101111	57	2F	/	Slash or divide
48	110000	60	30	0	Zero
49	110001	61	31	1	One
50	110010	62	32	2	Two
51	110011	63	33	3	Three
52	110100	64	34	4	Four
53	110101	65	35	5	Five
54	110110	66	36	6	Six
55	110111	67	37	7	Seven
56	111000	70	38	8	Eight
57	111001	71	39	9	Nine
58	111010	72	3A	:	Colon
59	111011	73	3B	;	Semicolon
60	111100	74	3C	<	Less than (or open angled bracket)
61	111101	75	3D	=	Equals
62	111110	76	3E	>	Greater than (or closeangled bracket)
63	111111	77	3F	?	Question mark
64	1000000	100	40	@	At symbol
65	1000001	101	41	A	Uppercase A
66	1000010	102	42	B	Uppercase B
67	1000011	103	43	C	Uppercase C
68	1000100	104	44	D	Uppercase D
69	1000101	105	45	E	Uppercase E
70	1000110	106	46	F	Uppercase F
71	1000111	107	47	G	Uppercase G
72	1001000	110	48	H	Uppercase H
73	1001001	111	49	I	Uppercase I
74	1001010	112	4A	J	Uppercase J
75	1001011	113	4B	K	Uppercase K
76	1001100	114	4C	L	Uppercase L
77	1001101	115	4D	M	Uppercase M
78	1001110	116	4E	N	Uppercase N
79	1001111	117	4F	O	Uppercase O
80	1010000	120	50	P	Uppercase P
81	1010001	121	51	Q	Uppercase Q
82	1010010	122	52	R	Uppercase R
83	1010011	123	53	S	Uppercase S
84	1010100	124	54	T	Uppercase T
85	1010101	125	55	U	Uppercase U
86	1010110	126	56	V	Uppercase V
87	1010111	127	57	W	Uppercase W
88	1011000	130	58	X	Uppercase X
89	1011001	131	59	Y	Uppercase Y
90	1011010	132	5A	Z	Uppercase Z
91	1011011	133	5B	[	Opening bracket
92	1011100	134	5C	\	Backslash
93	1011101	135	5D	]	Closing bracket
94	1011110	136	5E	^	Caret - circumflex
95	1011111	137	5F	_	Underscore
96	1100000	140	60	`	Grave accent
97	1100001	141	61	a	Lowercase a
98	1100010	142	62	b	Lowercase b
99	1100011	143	63	c	Lowercase c
100	1100100	144	64	d	Lowercase d
101	1100101	145	65	e	Lowercase e
102	1100110	146	66	f	Lowercase f
103	1100111	147	67	g	Lowercase g
104	1101000	150	68	h	Lowercase h
105	1101001	151	69	i	Lowercase i
106	1101010	152	6A	j	Lowercase j
107	1101011	153	6B	k	Lowercase k
108	1101100	154	6C	l	Lowercase l
109	1101101	155	6D	m	Lowercase m
110	1101110	156	6E	n	Lowercase n
111	1101111	157	6F	o	Lowercase o
112	1110000	160	70	p	Lowercase p
113	1110001	161	71	q	Lowercase q
114	1110010	162	72	r	Lowercase r
115	1110011	163	73	s	Lowercase s
116	1110100	164	74	t	Lowercase t
117	1110101	165	75	u	Lowercase u
118	1110110	166	76	v	Lowercase v
119	1110111	167	77	w	Lowercase w
120	1111000	170	78	x	Lowercase x
121	1111001	171	79	y	Lowercase y
122	1111010	172	7A	z	Lowercase z
123	1111011	173	7B	{	Opening brace
124	1111100	174	7C	|	Vertical bar
125	1111101	175	7D	}	Closing brace
126	1111110	176	7E	~	Equivalency sign - tilde
127	1111111	177	7F	DEL	Delete
# In[127]:


suppose 


# In[128]:


s = 'sudhanshu12 '


# In[129]:


s


# In[130]:


s.isalnum()


# In[131]:


s= 'sudhanshu123'


# In[132]:


s


# In[133]:


s.isalnum()


# In[134]:


s.center (20,'*')


# In[136]:


s = ' 5 '
s.isalnum()


# In[137]:


sw = "this is very first prgramming class"


# In[138]:


sw


# In[139]:


sw.isspace()

above one is false because string contain space inside string,
but its not space string completely as per the definition. 
# In[140]:


s = ' 6  '


# In[141]:


s.isspace()


# In[143]:


s = "554546"
s.isdigit()


# In[145]:


s1 = "eefefdfdf5544545"
s1.isnumeric()


# In[146]:


s1.isdigit()

Signature: s1.isnumeric()
Docstring:
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.
Type:      builtin_function_or_methodSignature: s1.isdigit()
Docstring:
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.
Type:      builtin_function_or_method
# In[147]:


s = "sudh"


# In[148]:


reversed(s)


# In[153]:


'd' .join("ineuron")


# In[154]:


"".join(reversed("sudh"))


# In[157]:


s = 'sudhanshu\tkumar\tineuron'


# In[158]:


s.expandtabs()


# In[159]:


s="Sudhanshu"
"".join(reversed(s))


# In[160]:


s="hhe\tgge\thhe"
s.expandtabs()

s = "this is My Frist Python programming class and i am learNING pythin string and its function"
1. Try to extract data from index one to index 300 with a jump of 3
2. Try to reverse a string without using reverse function
3. Try to split a string after conversion of entire string in uppercase
4. Try to convert the whole string into lower case
5. Try to capitalize the whole string 
6/ Write a difference between isalnum() and isalpha()
7. Try to give an example of expand tab
8. Give an example of strip, lstrip and rstrip 
9. Replace a string character by another character by taking your own example
10. Try to give a definition of string center function with and example
11. Write your own defintion of compiler and interpretor without copy paste from internet in your language 
12. Python is a interpreted of compiled langauge give a c;ear answer with your understanding 
13. Try to write a usecase of python with your understanding. 
# In[ ]:


https://codeshare.io/X8PY8Y


s = "this is My First Python programming class and i am learNING python string and its function"
1 . Try to extract data from index one to index 300 with a jump of 3 
2. Try to reverse a string without using reverse function 
3. Try to split a string after conversion of entire string in uppercase 
4. try to convert the whole string into lower case 
5 . Try to capitalize the whole string 
6 . Write a diference between isalnum() and isalpha()
7. Try to give an example of expand tab
8 . Give an example of strip , lstrip and rstrip 
9.  Replace a string charecter by another charector by taking your own example 
"sudhanshu"
10 . Try  to give a defination of string center function with and exmple 
11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
12 . Python is a interpreted of compiled language give a clear ans with your understanding 
13 . Try to write a usecase of python with your understanding 


We have to sent our jupyter notebook to shivan@ineuron.ai 
before next saturday class 21st may 
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




