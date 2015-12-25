# dota2-Teammatch

## Objective:
This python script aims to find team match of dota2 players by Steam ID.

## Requirement:
Python 2.7

Scrapy

## Usage:
1. Put a json file including steam ID under dotabuff/spiders, named Steam.json.

        {
            "members" : [ 
                          765611981XXXXXXXX, 
                          765611982XXXXXXXX,
                          ....
                        ]
                        
        }
  
2. ` scrapy crawl dotaspider -o output.json `
