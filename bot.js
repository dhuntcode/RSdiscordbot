// require the discord.js module
const Discord = require('discord.js');
const botSettings = require("./auth.json");

// create a new Discord client
const rundownBot = new Discord.Client();

activeMembers = [];

rundownBot.on("ready", () => {
  console.log('Bot is ready');
});

rundownBot.on('message', async message => {
//let activeuser = message.author;#
if (activeMembers.indexOf(message.author)) {
  activeMembers.push(message.author)
  console.log(activeMembers);
}

});

rundownBot.login(botSettings.token);