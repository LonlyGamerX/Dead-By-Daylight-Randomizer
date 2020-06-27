import {typeCharacters1} from './Arrays/CharacterTypes.js'
import {killersName0, survivorsName0} from './Arrays/characters.js'
import {survivorPerksN1, killerPerksN1} from './Arrays/perks.js'

const TypesCharacters = typeCharacters1[Math.floor(Math.random() * typeCharacters1.length)]

//Randomizing Character depending on if its a type survivor or type killer
if (TypesCharacters === "Killer") {
  var CharacterName = killersName0[Math.floor(Math.random() * killersName0.length)];
} 
else if (TypesCharacters === "Survivor") {
  var CharacterName = survivorsName0[Math.floor(Math.random() * survivorsName0.length)];
}

//Randomizing Character perks depending on if its killer or survivor
if (TypesCharacters === "Killer") {
  var perks1 = killerPerksN1[Math.floor(Math.random() * killerPerksN1.length)]
  var perks2 = killerPerksN1[Math.floor(Math.random() * killerPerksN1.length)]
  var perks3 = killerPerksN1[Math.floor(Math.random() * killerPerksN1.length)]
  var perks4 = killerPerksN1[Math.floor(Math.random() * killerPerksN1.length)]
} 
else if (TypesCharacters === "Survivor") {
  var perks1 = survivorPerksN1[Math.floor(Math.random() * survivorPerksN1.length)]
  var perks2 = survivorPerksN1[Math.floor(Math.random() * survivorPerksN1.length)]
  var perks3 = survivorPerksN1[Math.floor(Math.random() * survivorPerksN1.length)]
  var perks4 = survivorPerksN1[Math.floor(Math.random() * survivorPerksN1.length)]
}


//Colors for console
// Reset = "\x1b[0m"
// Bright = "\x1b[1m"
// Dim = "\x1b[2m"
// Underscore = "\x1b[4m"
// Blink = "\x1b[5m"
// Reverse = "\x1b[7m"
// Hidden = "\x1b[8m"

// FgBlack = "\x1b[30m"
// FgRed = "\x1b[31m"
// FgGreen = "\x1b[32m"
// FgYellow = "\x1b[33m"
// FgBlue = "\x1b[34m"
// FgMagenta = "\x1b[35m"
// FgCyan = "\x1b[36m"
// FgWhite = "\x1b[37m"

// BgBlack = "\x1b[40m"
// BgRed = "\x1b[41m"
// BgGreen = "\x1b[42m"
// BgYellow = "\x1b[43m"
// BgBlue = "\x1b[44m"
// BgMagenta = "\x1b[45m"
// BgCyan = "\x1b[46m"
// BgWhite = "\x1b[47m"


//showing the results in console
console.log('\x1b[36mOriginal creator - Scott - twitch.tv/LonlyGamerX');
console.log('');
console.log(`\x1b[32mCharacter type: \x1b[31m\x1b[4m${TypesCharacters}\x1b[0m`)
console.log(`\x1b[32mChracter name: \x1b[31m\x1b[4m${CharacterName}\x1b[0m`)
console.log('');
console.log(`\x1b[32mPerk 1: \x1b[31m\x1b[4m${perks1}\x1b[0m`)
console.log(`\x1b[32mPerk 2: \x1b[31m\x1b[4m${perks2}\x1b[0m`)
console.log(`\x1b[32mPerk 3: \x1b[31m\x1b[4m${perks3}\x1b[0m`)
console.log(`\x1b[32mPerk 4: \x1b[31m\x1b[4m${perks4}\x1b[0m`)