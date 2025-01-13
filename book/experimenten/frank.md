# Franck-Hertz experiment
practicumhandleiding  
*Deze handleiding is grotendeels overgenomen van de [Universiteit van Utrecht](https://nspracticum.science.uu.nl/Outreach/UP/Franck-Hertz/handleiding_Franck-Hertz.pdf).*

```{figure} ./media/franck/frank1.jpg
    :name: opstelling Frank
    :align: center 

Foto van de Franck-Hertz opstelling.
```

## Inleiding
Dit experiment werd voor het eerst gedaan in 1912 door James Franck en Gustav Hertz. Het is een sleutelexperiment van de quantummechanica, en Franck en Hertz kregen voor dit experiment de Nobelprijs voor Natuurkunde in 1925. 
Het Franck-Hertz experiment laat zien dat de energie die elektronen hebben als ze uit een atoom worden vrij gemaakt gequantiseerd is. Dat betekent dat de bindingsenergie van elektronen niet continu kan zijn, maar alleen specifieke waardes kan hebben. Deze observatie kan goed verklaard worden met het Bohr-model van atomen. 
Het mechanisme wat aan dit experiment ten grondslag ligt wordt nog steeds gebruikt in hoe TL-buizen werken. 

## Theorie
Om je goed voor te bereiden op het experiment wordt eerst de theorie bestudeerd. 

```{figure} ./media/franck/frank2.svg
   :width:100
   :name: bohrmodel
   :align: center
 Bohrmodel (bron: JabberWok uit en.wikipedia.org (CC))
```

### Bohrmodel 
In het Bohrmodel van een atoom bestaat een atoom uit een positief geladen kern met eromheen de negatief geladen elektronen. De elektronen in het Bohrmodel kunnen alleen in specifieke banen bestaan. Deze banen verschillen in hoeveel energie er nodig is om het elektron er uit te halen. We noemen de banen daarom ook wel energieschillen. Zie figuur. De energieschillen hebben een quantumgetal n. De kern heeft een lading van +Ze met Z het aantal protonen in de kern en e de elementaire lading. 

>#### Opdracht 1: Energie en golflengte 
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

```{figure} ./media/franck/frank3.jpg
    :name: schema
    :align: center 
 Het schakelschema (bron: https://physics.unimelb.edu.au/lecture-demonstrations/modern-physics/na-19-franck-hertz-experiment)
```

In de figuur staat de stroomkring van de Franck-Hertz opstelling getekend. Bij $C$, de kathode, komen elektronen vrij door genoeg spanning $U_F$ op het filament te zetten. Het filament gaat dan gloeien, en elektronen uitzenden. Deze elektronen worden versneld naar het rooster (grid) $G$ met een versnelspanning $U$. Het elektrisch veld zorgt voor een elektrische kracht op elk elektron van: 

```{math}
:label: 1
F_{elek} = q \cdot E_{elek} = q \cdot \frac{U}{L}
```


met $F_{elek}$ de kracht op het elektron, $q$ de lading van het elektron, $E_{elek}$ de elektrische veldsterkte, $U$ de aangelegde spanning in Volt, en $L$ de afstand tussen $C$ en $G$. 
Deze kracht zorgt ervoor dat het elektron versnelt volgens de tweede wet van Newton: $F = ma$. Vervolgens komen de versnelde elektronen aan bij de anode $A$ en wordt er een stroom gemeten. De tegenspanning $U_GA$ helpt ervoor te zorgen dat er geen elektronen per ongeluk bij de anode terecht komen, maar dat dit alleen elektronen zijn met voldoende snelheid. 


>#### Opdracht 2: Energie en botsen 
>Elektronen worden versneld in een elektrisch veld. Het elektrische veld leg je straks zelf aan door de spanning U en UGA in te stellen. 
> <br>
>a) Als er een tegenspanning UGA van 1 V wordt aangelegd, hoeveel (kinetische) energie heeft een elektron dan nodig om toch de anode te bereiken op het moment dat het elektron door het rooster gaat? 
> <br>
>b) Na een botsing verliest een elektron energie, en zal dus langzamer bewegen. Als het elektron zich dan nog in het elektrisch veld tussen $C$ en $G$ bevindt zal het weer versnellen tot het of tegen het rooster aan botst, of erdoorheen gaat op weg naar de anode. Hoever moet een elektron bewegen voordat het weer 5 eV aan kinetische energie heeft bij een versnelspanning van 20 V? L is ongeveel 1 cm. Gebruik: $E = 5 eV = W = Fs = q\frac{V}{L}s (2)$ met $E$ de energie van het elektron en $W = Fs$ de arbeid verricht door het elektrisch veld. 

## Uitvoering 
Je gaat nu aan de slag met de opstelling waarbij je eerst zal lezen over hoe de opstelling werkt en daarna een aantal proefmetingen zal uitvoeren. Op deze manier begrijp je goed hoe de opstelling werkt. Daarna ga je eigenlijke meting uitvoeren.

### De opstelling 
De opstelling bestaat uit de oven, een power supply (spanningsbron) en een een oscilloscoop, zie figuur 3. Bij de theorie heb je al een schematische tekening van de stroomkring in de opstelling gezien. Deze staat ook op de oven getekend. De draden zijn al goed aangesloten op de spanningsbron en de oscilloscoop. 

```{figure} ./media/frank4.png
    :name: opstelling
    :align: center 
De Franck-Hertz opstelling
```

>#### Opdracht 3: Klaar zetten 
>De oven wordt straks heet en dan kun je deze lastiger verplaatsen. Zorg dus nu vast dat je goed naar binnen kunt kijken. 
>1. Zet de oven zo neer dat je de voorkant, waar de draden aangesloten zijn, en het raam om naar binnen kunt kijken goed kunt zien. 
>2. Zet de oven aan en stel te temperatuur in op 180 ◦C. Het duurt 5 tot 10 minuten voordat de temperatuur bereikt is. PAS OP: ook de buitenkant van de oven wordt heet! 
>3. Draai de volgende knopjes op de power supply helemaal naar links (naar 0): de filamentspanning, de spanning tot het eerste grid (deze wordt niet gebruikt), de start- en eind spanning voor de versnelspanning, en de tegenspanning. Het knopje rechtsonder is de sterkte van het totale signiaal wat doorgestuurd wordt naar de oscilloscoop. Laat deze voor nu staan zoals die is (dus niet op 0!). 
>4. Zet de power supply (grijs blauwe kast) met de knop achterop aan. Opstarten kan even duren.
>5. Zet de oscilloscoop aan. 
>6.  Stel de oscilloscoop zo in dat signaal 1 op de x-as wordt weer gegeven en signaal 2 op de y-as (X-Y mode). Waarschijnlijk is dit al gebeurd. Eventueel doe je dit met het knopje Main en vervolgens op het scherm, selecteer met de knopjes net naast het scherm Time Base XY.

### Proefmeting 
Wanneer de oven is opgewarmd kan je beginnen met meten. De warme oven zorgt ervoor dat een klein druppeltje kwik wat in de vacuum buis zit verdampt. 

#### Opdracht 4: Proefmeting 
Met deze reeks proefmetingen leer de de oscilloscoop en de spanningsbron bedienen. 
1. Zet de filamentspanning op 6,0V tot 6,5 V. Zie je het filament oplichten (oranje)? Het duurt tot 60 seconden voordat het filament stabiel op de gewenste spanning brandt. 
2. Zet de tegenspanning (de uiterst rechtse knop) op 1.5 V. 
3. Zet de versnelspanning op manual met het zwarte knopje tussen de start- en eindspanningsdraaiknopjes (acceleration) op de power supply. Draai nu langzaam de eindversnelspanning omhoog. Zie je een stipje bewegen op het scherm van de oscilloscoop? Tot welke spanning kun je gaan voordat je een plasma krijgt (het blauwe licht bovenin de buis)? 
Let op: Als je de spanning te hoog zet dan slaat de stroom door: er ontstaat een plasma. Je kunt zien als dit gebeurt is: dan licht het kwikplasma fel en helderblauw op. Zet dan de spanning weer lager en probeer dit te voorkomen. 
4. Op het scherm van de power supply zie je ook hoe veel stroom (nA) er gemeten wordt. Het maximale wat deze opstelling kan meten is 400 nA. Bij welke spanning krijg je nog net geen 400 nA (en ook nog geen plasma)? Dit is de spanning die je nu als eindsspanning wilt gebruiken. (vaak 30V).
5. De ingestelde spanning staat op de x-as op de oscilloscoop, en de stroom die gemeten wordt bij de anode A staat op de y-as. Op het scherm van de oscilloscoop zie je hoeveel V of mV ´e´en hokje is. Deze kan je aanpassen met de draaiknopjes Volts/Div. (De grote draaiknoppen onder vertical). Zet deze beiden op 1 V/div. 
6. Zet nu de versnelspanning op Ramp (Weer het zwarte knopje bij accelaration op de power supply). De power supply geeft nu heel snel achter elkaar een spanning van de ingestelde start- tot de ingestelde eindspanning. Als het goed is zie je op het scherm van de oscilloscoop nu een curve die lijkt op figuur 4. 
  

figuur4

#### Opdracht 5: Optimalisatie 
Voor het meten straks is het handig om de curve optimaal in beeld te kunnen brengen. Hieronder staan een aantal tips over het effect van bepaalde instellingen. Je bent vrij om hiermee te experimenteren en ook om nog andere instellingen te proberen. Let er wel op de je probeert om te voorkomen dat je een plasma krijgt. 
1. start- en eind versnelspanning: deze kan je vrij kiezen. Wil je veel pieken en dalen achter elkaar zien, of juist maar een paar? Wil je op 0 beginnen? (Let op: dit hangt ook samen met hoe je de oscilloscoop in stelt, daarmee kan je ook ‘inzoomen’) 
2. In figuur 4 a) zie je dat de curve naar het maximum gaat (vlakke lijn bovenaan). Probeer dit te voorkomen: zet de eindversnelspanning lager! Als je toch meer pieken en dalen wilt kunnen zien, verander dan een andere instelling zodat je de eindspanning wel hoger kunt zetten zonder dit maximum te bereiken. 
3. In figuur 4 b) en c) is de curve te steil of te vlak. Dit kan je op verschillende manieren verbeteren: 
– Vernader de Volts/Div van kanaal 2. Dit is het herschalen van de data die je meet. 
– Verander de tegenspanning. Hiermee verander je de meting zelf: je maakt het makkelijker of moeilijker voor elektronen om de anode te bereiken. 

Deze oplossingen hebben een klein beetje een ander effect, bijvoorbeeld op hoe diep de dalen zijn. Kies zelf wat je het beste uit komt. 
4. De filamentspanning bepaald hoeveel elektronen er vrij komen. Bij een hogere filamentspanning meet je dus gemakkelijker meer stroom bij de anode. In figuur 4 d) is deze te hoog, en in figuur 4 e) te laag. Je wilt genoeg signaal hebben om te kunnen meten, maar niet zo veel dat je al snel bij het maximum (vlakke lijn aan de bovenkant) zit. Daarbij is een hoge filamentspanning (boven 10V) slecht voor de levensduur van het filament. 
5. Met de oscilloscoop kan je de weergave van je resultaten verbeteren. Zet de Volt/Div en Position van beide kanalen zo dat je curve goed in het midden en goed geschaald is. In het menu Display kan je ook het Type en Persist nog aanpassen. 

## 4 Onderzoeksvragen en werkplan

Na de theoretische voorbereiding en het verkennen van de opstelling kun je nu de onderzoeks vraag en een werkplan op te stellen. 
#### Opdracht 6: Interpretatie 
Je ziet nu dat de gemeten stroom pieken en dalen heeft bij verschillende versnelspanningen. 
1. Hoeveel kinetische energie heeft een elektron op een bepaalde plek tussen C en G? 
2. Hoe verandert de energie van een elektron wanneer dit genoeg energie heeft om een 
kwikatoom in een aangeslagen toestand te brengen door een inelastische botsing? 
3. Wat gebeurt er met een kwikatoom als dit een inelastische botsing heeft met een elektron wat veel energie heeft? 
4. Bij opdracht 2 heb je berekent hoe ver een elektron moet versnellen voordat het (weer) een bepaalde energie heeft. Als de afstand tussen C en G 1 cm is, hoe vaak kan een elektron dan botsen met een kwikatoom? 
5. Schets de energie van een elektron wanneer het van C, via G naar A reist. Zet de energie op de y-as, en de afgelegde afstand op de x-as. Hoe verandert dit wanneer de versnelspanning hoger is? 
6. Wat kun je zeggen over waarom er pieken en dalen zijn in de gemeten stroom bij verschillende spanningen? 

7. Wat betekent de afstand tussen de pieken (of de afstand tussen de dalen)? Verwacht je dat deze afhankelijk is van ´e´en van je instellingen? 

#### Opdracht 7: Onderzoeksvragen 
Formuleer de onderzoeksvraag die je met deze opstelling wilt beantwoorden. Gebruik hiervoor de kennis die je hebt opgedaan in de voorbereiding. Je moet de onderzoeksvraag kunnen beantwoorden met deze opstelling. Stel voor de onderzoeksvraag een hypothese op. De hypothese is wat je verwacht dat het antwoord zal zijn op de onderzoeksvraag. 

##### Opdracht 8: Werkplan 
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

## extra theoretische uitleg
bron: [UCSB Phyics Remote Labs](https://ilg.physics.ucsb.edu/Courses/RemoteLabs/?linkfile=FH_Remote#:~:text=Video%201-,Theory,the%20anode%20and%20the%20cathode). 

### Het Franck-Hertz-experiment: uitleg en interpretatie

Het Franck-Hertz-experiment genereert vrije elektronen door een kathode te verhitten in een vacuümbuis. Deze elektronen worden versneld richting een anode door een spanningsverschil (\(V_a\)) tussen de kathode en anode. Terwijl de elektronen bewegen, krijgen ze kinetische energie \(eV_a\), tenzij ze onderweg botsen met een ander deeltje en een inelastische botsing ondergaan.

Hoewel de buis geëvacueerd is, is deze niet volledig leeg. Er bevindt zich een kleine hoeveelheid kwikdamp in de buis. Kwik is vloeibaar bij kamertemperatuur, maar door de buis te verhitten wordt een lage druk gas van kwikatomen gevormd tussen de kathode en anode. Bewegende elektronen kunnen botsen met deze kwikatomen en kinetische energie verliezen.

#### Elastische versus inelastische botsingen
- **Elastische botsingen:** Hierbij verandert de kinetische energie van het elektron nauwelijks, omdat een kwikatoom veel zwaarder is dan een elektron.
- **Inelastische botsingen:** Hierbij verliezen elektronen een specifiek hoeveelheid energie, gelijk aan het verschil tussen energieniveaus van het kwikatoom.

#### Energieovergangen in kwik
Kwikatomen kunnen alleen discrete hoeveelheden energie absorberen, zoals de eerste excitatie-energie van **4,66 eV** (het energieverschil tussen de grondtoestand \(n=1\) en de eerste aangeslagen toestand \(n=2\)). Dit betekent dat elektronen alleen energie verliezen als hun kinetische energie groter is dan of gelijk is aan deze waarde. Dit discrete gedrag is een fundamenteel kenmerk van kwantummechanica.

### Hoe werkt het experiment?
Door de spanning \(V_a\) geleidelijk te verhogen, meet je het aantal elektronen dat de anode bereikt. Zodra \(eV_a = 4,66 \, \text{eV}\), hebben de elektronen voldoende energie om een kwikatoom te exciteren en verliezen ze kinetische energie. Hierdoor ontstaat een daling in de stroom naar de anode. Deze spanning (\(V_1\)) wordt de eerste excitatiespanning genoemd.

Bij hogere spanningen kunnen elektronen meerdere inelastische botsingen ondergaan:
- Bij \(V_a > 2V_1\) kunnen elektronen twee botsingen ondergaan.
- Bij \(V_a > 3V_1\) zijn drie botsingen mogelijk, enzovoort.

Dit leidt tot een patroon van opeenvolgende dalingen in de gemeten stroom bij spanningen van \(V_1\), \(2V_1\), \(3V_1\), enzovoort.

#### Afwijkingen tussen theorie en experiment
In het experiment worden vaak waarden van **4,9 eV** of **4,96 eV** gemeten in plaats van de theoretische waarde van **4,66 eV**. Dit kan komen door:
1. **Systematische fouten:** Zoals kleine spanningsverschillen door contactpotentialen.
2. **Meetomstandigheden:** Zoals druk en temperatuur van de kwikdamp.
3. **Afgeronde waarden:** Experimentele resultaten worden vaak benaderd voor eenvoud.

#### Het meten van stroom
Een extra complicatie is dat het niet direct mogelijk is om de kinetische energie van de elektronen te meten. In plaats daarvan wordt de stroom naar een collectorelektrode gemeten. Als elektronen onderweg kinetische energie verliezen, verlaagt dit de stroom.

### Conclusie
Het Franck-Hertz-experiment laat zien dat kwikatomen energie absorberen in discrete stappen, wat een direct bewijs is van de kwantummechanische theorie. Hoewel de gemeten waarde van \(V_1\) vaak iets hoger is dan de theoretische waarde (bijvoorbeeld **4,96 eV** in plaats van **4,66 eV**), ondersteunt het experiment duidelijk de kwantisatie van energieniveaus.

### Video uitleg 
<div style="display: flex; justify-content: center;">
<div style="position: relative; width: 70%; height: 0; padding-bottom: 56.25%;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jckgt5X9p60?si=8oqSXR1DZ1IqeKvk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
</div>