<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Pepper_trialQuiz" format_version="4">
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
        <File name="GlobeAsiaAustralia" src="html/GlobeAsiaAustralia.png" />
        <File name="Koalas" src="html/Koalas.jpg" />
        <File name="Scroll" src="html/Scroll.png" />
        <File name="Seedling" src="html/Seedling.png" />
        <File name="SirJohnMonash" src="html/SirJohnMonash.jpg" />
        <File name="SlightlySmileFace" src="html/SlightlySmileFace.gif" />
        <File name="SoccerBall" src="html/SoccerBall.png" />
        <File name="ThinkingFace" src="html/ThinkingFace.gif" />
        <File name="kangaroo" src="html/kangaroo.png" />
        <File name="musicalscore" src="html/musicalscore.png" />
        <File name="AustralianBill" src="html/AustralianBill.jpg" />
        <File name="AusCapital" src="html/AusCapital.jpeg" />
        <File name="FETCH_HEAD" src=".git/FETCH_HEAD" />
        <File name="HEAD" src=".git/HEAD" />
        <File name="config" src=".git/config" />
        <File name="description" src=".git/description" />
        <File name="applypatch-msg" src=".git/hooks/applypatch-msg.sample" />
        <File name="commit-msg" src=".git/hooks/commit-msg.sample" />
        <File name="fsmonitor-watchman" src=".git/hooks/fsmonitor-watchman.sample" />
        <File name="post-update" src=".git/hooks/post-update.sample" />
        <File name="pre-applypatch" src=".git/hooks/pre-applypatch.sample" />
        <File name="pre-commit" src=".git/hooks/pre-commit.sample" />
        <File name="pre-merge-commit" src=".git/hooks/pre-merge-commit.sample" />
        <File name="pre-push" src=".git/hooks/pre-push.sample" />
        <File name="pre-rebase" src=".git/hooks/pre-rebase.sample" />
        <File name="pre-receive" src=".git/hooks/pre-receive.sample" />
        <File name="prepare-commit-msg" src=".git/hooks/prepare-commit-msg.sample" />
        <File name="update" src=".git/hooks/update.sample" />
        <File name="exclude" src=".git/info/exclude" />
        <File name="bootstrap.min" src="html/styles/bootstrap.min.css" />
        <File name="jquery-ui.min" src="html/styles/jquery-ui.min.css" />
        <File name="AncoraImparo_Motto" src="html/AncoraImparo_Motto.png" />
        <File name="FirstFleet" src="html/FirstFleet.jpg" />
        <File name="OperaHouse" src="html/OperaHouse.jpg" />
        <File name="phobia" src="html/phobia.png" />
        <File name="river" src="html/river.jpg" />
        <File name="sports" src="html/sports.jpg" />
        <File name="icon" src="icon.png" />
        <File name="results" src="results.py" />
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
