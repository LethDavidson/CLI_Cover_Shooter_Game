# CLI_Cover_Shooter_Game
The code for a turn based cover shooter game in python. Features mission selection, weapons, destructible cover, ect.

Sound effects for weapons, and alien pain are from SoundBible.com and are not my own creation
Sectoid death sound is owned by 2k Games, I claim no ownership.
All music is owned by copyrighted sources, I claim no ownership over it  and will not use them in a commerical avenue.

COMBAT:Stores combat features. No self functions as it's not really used anywhere other than itslef.
Player and enemies take turns, lotsa functions for compartlamentalization of combat.
Player chooses cover, takes an action, ends their turn. Aliens dot he same, their turn ends.

Cover: Holds info for cover objects. Cover has HP, defense ]buffing, aim alterization.
Cover can break. Cover is generated and then stored in a list that is used for combat and briefing.

Grenade:Stores grenade info. Later this will be made into just an item subclass

GUIPygame:Remnants of fucking with pyGame for GUI.

Healing:Medkits and healing class. Probably should be an item subvlass as well.

Items: creates game items like ammo belts and magazines. Has multiple subclasses.
This info is sent to pickLoadout and for generation of game actors.

Main:Where all the differing game tpes are held and it operates the main game loop.

MIssionGenerator: creates all of the game actors that will be used elsewhere in the program. 
Creates user/useable pod/cover/briefing/ect. Gets ifnot hat player will use for picking thier mission.

pickLoadout:Picks all weapons/ammo/items/ect that player will yse after selecting which mission they will go on.

Player:Holds info for the player actor.Holds all player weapons, items, actions, variables, anything the player will need.

Pods: Creates the pods that are used in mission generation. Creates lsits that are put into a dict which are then chosen by random.
It's rather easy to add new pods by building a config and adding it to storage.

Sectoid: Holds all actor object data for the sectoid enemy type. Rather underdeveloped and full of my oldest code.

Sound:Holds all sound data using pygame mixer code. creates here and called/put iinto variables elsewhere.

test:Place to fuck around with code ideas.

Weapons: Holds all weapons data. Shooting and reloading is handled by the weapon object.
Bullet subclass is also here, and new attributes can be added to bullets that go in magaziens which go in guns.

worldmap:Lets you pick the mission you are going to play using the mission generation data.
This needs to delete old missions after one is completed but does not right now.
