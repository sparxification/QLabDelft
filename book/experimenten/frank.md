# Franck-Hertz experiment
practicumhandleiding  
*Deze handleiding is grotendeels overgenomen van de Universiteit van Utrecht*

```{figure} ./media/frank1.png
    ---
    width:5
    name: opstelling Frank
    align: center 
    ---
Foto van de Franck-Hertz opstelling (van 3Bscientific)
```

## Inleiding
Dit experiment werd voor het eerst gedaan in 1912 door James Franck en Gustav Hertz. Het is een sleutelexperiment van de quantummechanica, en Franck en Hertz kregen voor dit experiment de Nobelprijs voor Natuurkunde in 1925. 
Het Franck-Hertz experiment laat zien dat de energie die elektronen hebben als ze uit een atoom worden vrij gemaakt gequantiseerd is. Dat betekent dat de bindingsenergie van elektronen niet continu kan zijn, maar alleen specifieke waardes kan hebben. Deze observatie kan goed verklaard worden met het Bohr-model van atomen. 
Het mechanisme wat aan dit experiment ten grondslag ligt wordt nog steeds gebruikt in hoe TL-buizen werken. 

## Theorie
Om je goed voor te bereiden op het experiment wordt eerst de theorie bestudeerd. 

```{figure} ./media/frank2.svg
   ---
   width:50
   name: bohrmodel
   align: right 
   ---
 figuur 1
```

### Bohrmodel 
In het Bohrmodel van een atoom bestaat een atoom uit een positief geladen kern met eromheen de negatief geladen elektronen. De elektronen in het Bohrmodel kunnen alleen in specifieke banen bestaan. Deze banen verschillen in hoeveel energie er nodig is om het elektron er uit te halen. We noemen de banen daarom ook wel energieschillen. Zie figuur 1. De energieschillen hebben een quantumgetal n. De kern heeft een lading van +Ze met Z het aantal protonen in de kern en e de elementaire lading. 

>Opdracht 1: Energie en golflengte 
>Als een elektron uit een hogere schil terug valt in een lagere schil verliest het elektron energie. 
<br>
>a) Welke golflengte (in nm) heeft licht met een energie van 4.9 eV? <br>
>b) Verwacht je deze kleur te kunnen zien? Zo ja, welke kleur is het? 

In dit experiment ga je bewijzen dat elektronen in kwikatomen alleen bij specifieke energie voorkomen. 

### Elektron-atoom botsingen
In de klassieke mechanica van Newton geeft een botsend object (kinetische) energie door aan het gebotste object. Bijvoorbeeld: als de witte biljartbal tegen de rode stoot dan blijft na de elastische botsing de witte stil liggen op de plek van de botsing en beweegt de rode verder. Dit is een elastisch botsing. Kinetisch energie van de witte biljartbal wordt omgezet in kinetische energie van de rode biljartbal. 
Een ander type botsing is een inelastische botsing. Dit is wanneer de kinetische energie wordt omgezet in een ander type energie, bijvoorbeeld warmte, of geluid, of het kreukelen van een auto. 
Elektronen kunnen ook een elastische of inelastische botsingen met atomen hebben. Bijvoorbeeld wanneer een elektron beweegt in een elektrisch veld, en een atoom in de gasfase op het pad tegen komt. 
Bij een elastische botsing veranderen de snelheden van het atoom en het elektron. Omdat het atoom zo veel zwaarder is dan een elektron zal het atoom nauwelijks van richting of snelheid veranderen na een elastische botsing. 
Bij een inelastische botsing wordt de kinetische energie van het elektron geabsorbeerd door het atoom, waardoor het atoom in een aangeslagen toestand komt. De aangeslagen toestand betekent dat een elektron van het atoom zelf in een hogere baan terecht is gekomen. In dit experiment zul je zien dat alleen elektronen met een bepaalde energie een inelastische botsing kunnen hebben met kwikatomen. Dit is een gevolg van de elektron-schillen van atomen en is niet te verklaren met klassieke mechanica, maar wel met quantummechanica! 

```{figure} ./media/frank3.png
    ---
    width:100
    name: schema
    align: center 
    ---
 figuur 2: Het schakelschema
```

In figuur 2 staat de stroomkring van de Franck-Hertz opstelling getekend. Bij $C$, de kathode, komen elektronen vrij door genoeg spanning $U_F$ op het filament te zetten. Het filament gaat dan gloeien, en elektronen uitzenden. Deze elektronen worden versneld naar het rooster (grid) $G$ met een versnelspanning $U$. Het elektrisch veld zorgt voor een elektrische kracht op elk elektron van: 

```{math}
:label: 1
F_elek = q \cdot E_elek = q \cdot \frac{U}{L}
```


met $F_elek$ de kracht op het elektron, $q$ de lading van het elektron, $E_elek$ de elektrische veldsterkte, $U$ de aangelegde spanning in Volt, en $L$ de afstand tussen $C$ en $G$. 
Deze kracht zorgt ervoor dat het elektron versnelt volgens de tweede wet van Newton: $F = ma$. Vervolgens komen de versnelde elektronen aan bij de anode $A$ en wordt er een stroom gemeten. De tegenspanning $U_GA$ helpt ervoor te zorgen dat er geen elektronen per ongeluk bij de anode terecht komen, maar dat dit alleen elektronen zijn met voldoende snelheid. 


>Opdracht 2: Energie en golflengte 
>Elektronen worden versneld in een elektrisch veld. Het elektrische veld leg je straks zelf >aan door de spanning U en UGA in te stellen. 
> <br>
>a) Als er een tegenspanning UGA van 1 V wordt aangelegd, hoeveel (kinetische) energie heeft >een elektron dan nodig om toch de anode te bereiken op het moment dat het elektron door het >rooster gaat? 
> <br>
>b) Na een botsing verliest een elektron energie, en zal dus langzamer bewegen. Als het >elektron zich dan nog in het elektrisch veld tussen C en G bevindt zal het weer versnellen >tot het of tegen het rooster aan botst, of erdoorheen gaat op weg naar de anode. Hoever moet >een elektron bewegen voordat het weer 5 eV aan kinetische energie heeft bij een >versnelspanning van 20 V? L is ongeveel 1 cm. Gebruik: E = 5 eV = W = F s = qVLs (2) 
>met E de energie van het elektron en W = F s de arbeid verricht door het elektrisch veld. 

## Uitvoering 
Je gaat nu aan de slag met de opstelling waarbij je eerst zal lezen over hoe de opstelling werkt en daarna een aantal proefmetingen zal uitvoeren. Op deze manier begrijp je goed hoe de opstelling werkt. Daarna ga je eigenlijke meting uitvoeren.

### De opstelling 
De opstelling bestaat uit de oven, een power supply (spanningsbron) en een een oscilloscoop, zie figuur 3. Bij de theorie heb je al een schematische tekening van de stroomkring in de opstelling gezien. Deze staat ook op de oven getekend. De draden zijn al goed aangesloten op de spanningsbron en de oscilloscoop. 

```{figure} ./media/frank4.png
    ---
    width:100
    name: opstelling
    align: center 
    ---
 figuur 3: De Franck-Hertz opstelling
```

Opdracht 3: Klaar zetten 
De oven wordt straks heet en dan kun je deze lastiger verplaatsen. Zorg dus nu vast dat je goed naar binnen kunt kijken. 
 Zet de oven zo neer dat je de voorkant, waar de draden aangesloten zijn, en het raam om naar binnen kunt kijken goed kunt zien. 
Zet de oven aan en stel te temperatuur in op 180 ◦C. Het duurt 5 tot 10 minuten voordat de temperatuur bereikt is. PAS OP: ook de buitenkant van de oven wordt heet! 
 Draai de volgende knopjes op de power supply helemaal naar links (naar 0): de filamentspanning, de spanning tot het eerste grid (deze wordt niet gebruikt), de start- en eind spanning voor de versnelspanning, en de tegenspanning. Het knopje rechtsonder is de sterkte van het totale signiaal wat doorgestuurd wordt naar de oscilloscoop. Laat deze voor nu staan zoals die is (dus niet op 0!). 
 Zet de oscilloscoop aan met de knop bovenop. 
 Stel de oscilloscoop zo in dat signaal 1 op de x-as wordt weer gegeven en signaal 2 op de y-as. Dit doe je met het knopje Display en dan op het scherm, selecteer met de knopjes net naast het scherm Format XY. 

3.2 Proefmeting 
Wanneer de oven is opgewarmd kan je beginnen met meten. De warme oven zorgt ervoor dat een klein druppeltje kwik wat in de vacuum buis zit verdampt. Je kunt ook al testmetingen ¨ doen voordat de oven helemaal warm is, maar je signaal zal dan iets langer zijn omdat er nog iets minder kwik in de gasfase is. 

Opdracht 4: Proefmeting 
Met deze reeks proefmetingen leer de de oscilloscoop en de spanningsbron bedienen. a) Zet de filamentspanning op 7 V. Zie je het filament oplichten? Het duurt tot60 seconden voordat het filament stabiel op de gewenste spanning brandt. b) Zet de tegenspanning op 1.5 V. 
c) Zet de versnelspanning op manual met het zwarte knopje tussen de star- en eindspan ningsdraaiknopjes op de power supply. Draai nu langzaam de eindversnelspanning omhoog. Zie je een stipje bewegen op het scherm van de oscilloscoop? Tot welke spanning kun je gaan voordat je een plasma krijgt? 
Let op: Als je de spanning te hoog zet dan slaat de stroom door: er ontstaat een plasma. Je kunt zien als dit gebeurt is: dan licht het kwikplasma fel en helderblauw op. Zet dan de spanning weer lager en probeer dit te voorkomen. 
d) Op het scherm van de power supply zie je ook hoe veel stroom (nA) er gemeten wordt. Het maximale wat deze opstelling kan meten is 400 nA. Bij welke spanning krijg je nog net geen 400 nA (en ook nog geen plasma)? Dit is de spanning die je nu als eindsspanning wilt gebruiken. 
e) De ingestelde spanning staat op de x-as op de oscilloscoop, en de stroom die gemeten wordt bij de anode A staat op de y-as. Op het scherm van de oscilloscoop zie je hoeveel V of mV ´e´en hokje is. Deze kan je aanpassen met de draaiknopjes Volts/Div. Zet deze beiden op 1 V/div. 
f) Zet nu de versnelspanning op Ramp. De power supply geeft nu heel snel acher elkaar een spanning van de ingestelde start- tot de ingestelde eindspanning. Als het goed is zie je op het scherm van de oscilloscoop nu een curve die lijkt op figuur 4. 


figuur4

Opdracht 5: Optimalisatie 
Voor het meten straks is het handig om de curve optimaal in beeld te kunnen brengen. Hieronder staan een aantal tips over het effect van bepaalde instellingen. Je bent vrij om hiermee te experimenteren en ook om nog andere instellingen te proberen. Let er wel op de je probeert om te voorkomen dat je een plasma krijgt. 
 start- en eind versnelspanning: deze kan je vrij kiezen. Wil je veel pieken en dalen achter elkaar zien, of juist maar een paar? Wil je op 0 beginnen? (Let op: dit hangt ook samen met hoe je de oscilloscoop in stelt, daarmee kan je ook ‘inzoomen’) 
 In figuur 4 a) zie je dat de curve naar het maximum gaat (vlakke lijn bovenaan). Probeer dit te voorkomen: zet de eindversnelspanning lager! Als je toch meer pieken en dalen wilt kunnen zien, verander dan een andere instelling zodat je de eindspanning wel hoger kunt zetten zonder dit maximum te bereiken. 
 In figuur 4 b) en c) is de curve te steil of te vlak. Dit kan je op verschillende manieren verbeteren: 
– Vernader de Volts/Div van kanaal 2. Dit is het herschalen van de data die je meet. 
– Verander de tegenspanning. Hiermee verander je de meting zelf: je maakt het makkelijker of moeilijker voor elektronen om de anode te bereiken. 

Deze oplossingen hebben een klein beetje een ander effect, bijvoorbeeld op hoe diep de dalen zijn. Kies zelf wat je het beste uit komt. 
 De filamentspanning bepaald hoeveel elektronen er vrij komen. Bij een hogere fi lamentspanning meet je dus gemakkelijker meer stroom bij de anode. In figuur 4 d) is deze te hoog, en in figuur 4 e) te laag. Je wilt genoeg signaal hebben om te kunnen meten, maar niet zo veel dat je al snel bij het maximum (vlakke lijn aan de bovenkant) zit. Daarbij is een hoge filamentspanning (boven 10V) slecht voor de levensduur van het filament. 
 Met de oscilloscoop kan je de weergave van je resultaten verbeteren. Zet de Volt/Div en Position van beide kanalen zo dat je curve goed in het midden en goed geschaald is. In het menu Display kan je ook het Type en Persist nog aanpassen. 

4 Onderzoeksvragen en werkplan

Na de theoretische voorbereiding en het verkennen van de opstelling kun je nu de onderzoeks vraag en een werkplan op te stellen. 
Opdracht 6: Interpretatie 
Je ziet nu dat de gemeten stroom pieken en dalen heeft bij verschillende versnelspanningen. a) Hoeveel kinetische energie heeft een elektron op een bepaalde plek tussen C en G? b) Hoe verandert de energie van een elektron wanneer dit genoeg energie heeft om een 
kwikatoom in een aangeslagen toestand te brengen door een inelastische botsing? c) Wat gebeurt er met een kwikatoom als dit een inelastische botsing heeft met een elektron wat veel energie heeft? 
d) Bij opdracht 2 heb je berekent hoe ver een elektron moet versnellen voordat het (weer) een bepaalde energie heeft. Als de afstand tussen C en G 1 cm is, hoe vaak kan een elektron dan botsen met een kwikatoom? 
e) Schets de energie van een elektron wanneer het van C, via G naar A reist. Zet de energie op de y-as, en de afgelegde afstand op de x-as. Hoe verandert dit wanneer de versnelspanning hoger is? 
f) Wat kun je zeggen over waarom er pieken en dalen zijn in de gemeten stroom bij verschillende spanningen? 

g) Wat betekent de afstand tussen de pieken (of de afstand tussen de dalen)? Verwacht je dat deze afhankelijk is van ´e´en van je instellingen? 
Opdracht 7: Onderzoeksvragen 
Formuleer de onderzoeksvraag die je met deze opstelling wilt beantwoorden. Gebruik hiervoor de kennis die je hebt opgedaan in de voorbereiding. Je moet de onderzoeksvraag kunnen beantwoorden met deze opstelling. Stel voor de onderzoeksvraag een hypothese op. De hypothese is wat je verwacht dat het antwoord zal zijn op de onderzoeksvraag. 
Opdracht 8: Werkplan 
Stel nu het werkplan op waarin in ieder geval de volgende punten behandeld worden:  De onderzoeksvraag en hypothese. 
 De grootheden die gevarieerd worden. 
 De grootheden die gemeten worden en hoe deze metingen gedaan worden.  Het aantal metingen. 
 Hoe de data weergegeven wordt. 
5 Metingen 
Nadat je de voorbereiding hebt uitgevoerd en het werkplan is goedgekeurd door de docent of assistent, kan je het experiment gaan uitvoeren. 
Opdracht 9: Metingen 
Zoek met behulp van de meetopstelling volgens je werkplan een antwoord op de onder zoeksvraag en controleer de opgestelde hypothese. 
6 Rapportage 
Afhankelijk van wat je docent van je verwacht rapporteer je met een schriftelijk verslag of een presentatie over het onderzoek. Zorg ervoor dat in dit verslag of deze presentatie de volgende onderdelen duidelijk naar voren komen: 
 De onderzoeksvraag en hypothese. 
 Een beschrijving en een uitleg van de werking van de 
