Feature: Provide automatic comment base on the number of items
	As a user
	I want to have an automatic comment base on the number tasks
	So I can know how busy i'm

Scenario Outline: opening page
	Given I am opening the web page
	When I see <numberofitems> item's in my to do list
	Then I see a <comment> about how busy i'm
	Examples:
		|	numberofitems	| comment 					|
		|	0				| "yey, waktunya berlibur" 	|
		|	3				| "sibuk tapi santai"		|
		|	5				| "Semangat, kerja keras!"	|
		|	9				| "oh tidak"				|
