<?xml version="1.0" encoding="UTF-8" ?>
<Package name="start" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="concept" src="concept/concept.dlg" />
        <Dialog name="drink" src="drink/drink.dlg" />
        <Dialog name="food" src="food/food.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="concept_enu" src="concept/concept_enu.top" topicName="concept" language="en_US" />
        <Topic name="drink_enu" src="drink/drink_enu.top" topicName="drink" language="en_US" />
        <Topic name="food_enu" src="food/food_enu.top" topicName="food" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
</Package>
