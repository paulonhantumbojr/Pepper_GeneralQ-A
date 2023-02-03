<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Pepper_finalTest" format_version="4">
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
        <File name="bootstrap.min" src="html/styles/bootstrap.min.css" />
        <File name="jquery-ui.min" src="html/styles/jquery-ui.min.css" />
        <File name="icon" src="icon.png" />
        <File name="printer" src="printer.py" />
        <File name="template" src="template.html" />
        <File name="bootstrap.bundle.min" src="html/javascripts/bootstrap.bundle.min.js" />
        <File name="jquery-ui.min" src="html/javascripts/jquery-ui.min.js" />
        <File name="jquery.min" src="html/javascripts/jquery.min.js" />
        <File name="main-old" src="html/javascripts/main-old.js" />
        <File name="ui-icons_444444_256x240" src="html/styles/images/ui-icons_444444_256x240.png" />
        <File name="ui-icons_555555_256x240" src="html/styles/images/ui-icons_555555_256x240.png" />
        <File name="ui-icons_777620_256x240" src="html/styles/images/ui-icons_777620_256x240.png" />
        <File name="ui-icons_777777_256x240" src="html/styles/images/ui-icons_777777_256x240.png" />
        <File name="ui-icons_cc0000_256x240" src="html/styles/images/ui-icons_cc0000_256x240.png" />
        <File name="ui-icons_ffffff_256x240" src="html/styles/images/ui-icons_ffffff_256x240.png" />
        <File name="service" src="service.py" />
        <File name="AncoraImparo_Motto" src="html/images/AncoraImparo_Motto.png" />
        <File name="AusCapital" src="html/images/AusCapital.jpeg" />
        <File name="AustralianBill" src="html/images/AustralianBill.jpg" />
        <File name="Downward arrow" src="html/images/Downward arrow.png" />
        <File name="FingerDown" src="html/images/FingerDown.gif" />
        <File name="FirstFleet" src="html/images/FirstFleet.jpg" />
        <File name="GlobeAsiaAustralia" src="html/images/GlobeAsiaAustralia.png" />
        <File name="Koalas" src="html/images/Koalas.jpg" />
        <File name="Monash_Blue" src="html/images/Monash_Blue.png" />
        <File name="OperaHouse" src="html/images/OperaHouse.jpg" />
        <File name="Scroll" src="html/images/Scroll.png" />
        <File name="Seedling" src="html/images/Seedling.png" />
        <File name="SirJohnMonash" src="html/images/SirJohnMonash.jpg" />
        <File name="SlightlySmileFace" src="html/images/SlightlySmileFace.gif" />
        <File name="SoccerBall" src="html/images/SoccerBall.png" />
        <File name="ThinkingFace" src="html/images/ThinkingFace.gif" />
        <File name="kangaroo" src="html/images/kangaroo.png" />
        <File name="phobia" src="html/images/phobia.png" />
        <File name="river" src="html/images/river.jpg" />
        <File name="sports" src="html/images/sports.jpg" />
        <File name="waving-hand_hello" src="html/images/waving-hand_hello.gif" />
        <File name="braingear" src="html/images/braingear.png" />
        <File name="settings" src=".vscode/settings.json" />
        <File name="launch" src="html/.vscode/launch.json" />
        <File name="green_arrow2" src="html/images/green_arrow2.PNG" />
        <File name="README" src="README.md" />
        <File name="ScoreAplus" src="html/images/ScoreAplus.png" />
        <File name="Circle" src="html/images/Circle.png" />
        <File name="Square" src="html/images/Square.png" />
        <File name="Triangle" src="html/images/Triangle.png" />
        <File name="Q1 - Shape Cluster" src="html/videos/Q1 - Shape Cluster.mp4" />
        <File name="Puzzle_Piece" src="html/images/Puzzle_Piece.png" />
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
