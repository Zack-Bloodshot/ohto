{
      "name": "Ohto Ai Music Bot",
      "description": "An Anime themed Telegram group call music player bot.",
      "keywords": [
         "telegram",
         "anime",
         "group",
      ],   
   "repository": "https://github.com/Zack-Bloodshot/ohto ",
   "addons": [
      {
         "options": {
            "version": "12"
         },
         "plan": "heroku-postgresql"
      }
   ],
   "env": {
      "TOKEN": {
         "description": "Your bot token. Get one from @BotFather duh",
         "required": true,
         "value": ""
      },
      "API_ID": {
         "description": "Get API_ID from my.telegram.org, used for telethon based modules.",
         "required": true,
         "value": ""
      },
      "API_HASH": {
         "description": "Get API_HASH from my.telegram.org, used for telethon based modules.",
         "required": true,
         "value": ""
      },    
      "Mongo_db_URI": {
         "description": "Your Mongo db uri",
         "required": false,
         "value": ""
      },      
      "Sudo_users": {
         "description": "Your user ID as an integer.",
         "required": true,
         "value": ""
      }
      "Group": {
         "description": "The id where the bot will play",
         "required": true,
         "value": "-1001280998345"
      },
      "User_must_join": {
          "description": "I know this", 
          "required": false,
          "value": "no"
      }, 
      "Max_Dur": {
          "description": "The max duration of the video", 
          "required": true,
          "value": "6",
      }, 
      
   }
}