<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Survey_Encouragement" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="main" src="html/javascripts/main.js" />
        <File name="main.min" src="html/javascripts/main.min.js" />
        <File name="polyfill" src="html/javascripts/polyfill.js" />
        <File name="polyfill.min" src="html/javascripts/polyfill.min.js" />
        <File name="Raleway-Black" src="html/styles/fonts/Raleway-Black.ttf" />
        <File name="Raleway-Regular" src="html/styles/fonts/Raleway-Regular.ttf" />
        <File name="main" src="html/styles/main.css" />
        <File name="index" src="html/index.html" />
        <File name="service" src="service.py" />
        <File name="README" src="README.md" />
        <File name="Monash_Logo" src="html/Monash_Logo.jpg" />
        <File name="AustraliaFlag" src="html/AustraliaFlag.png" />
        <File name="GlobeAsiaAustralia" src="html/GlobeAsiaAustralia.png" />
        <File name="GoldenWattleFlower" src="html/GoldenWattleFlower.jpg" />
        <File name="HuntsmanSpider" src="html/HuntsmanSpider.jpg" />
        <File name="Koalas" src="html/Koalas.jpg" />
        <File name="MonashCampus" src="html/MonashCampus.png" />
        <File name="Scroll" src="html/Scroll.png" />
        <File name="Seedling" src="html/Seedling.png" />
        <File name="SirJohnMonash" src="html/SirJohnMonash.jpg" />
        <File name="SlightlySmileFace" src="html/SlightlySmileFace.gif" />
        <File name="SoccerBall" src="html/SoccerBall.png" />
        <File name="ThinkingFace" src="html/ThinkingFace.gif" />
        <File name="handclock" src="html/handclock.jpg" />
        <File name="kangaroo" src="html/kangaroo.png" />
        <File name="musicalscore" src="html/musicalscore.png" />
        <File name="AustralianBill" src="html/AustralianBill.jpg" />
        <File name="AboriginalAustralia" src="html/AboriginalAustralia.png" />
        <File name="MonashEngineering" src="html/MonashEngineering.jpg" />
        <File name="icon" src="icon.png" />
    </Resources>
    <Topics />
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
    <service name="service" autorun="true" execStart="./python service.py" />
    <executableFiles>
        <file path="python" />
    </executableFiles>
    <qipython name="service" />
</Package>
