console.log("Iniciando bot...");
const { Telegraf, Markup } = require('telegraf');

const bot = new Telegraf('8448288583:AAEy2QB12p0039Y_Eng8gAvFp3XQHcuQHWg');

// ----------------------------
//        COMANDO /start
// ----------------------------
bot.start((ctx) => {
    ctx.reply(
        '¡Hola! Soy tu bot. ¿Qué necesitas? 🤖',
        Markup.inlineKeyboard([
            [Markup.button.callback('Saludar 👋', 'OP_HOLA')],
            [Markup.button.callback('¿Cómo estás? 🤔', 'OP_ESTAS')],
            [Markup.button.callback('Número Random 🔢', 'OP_RANDOM_NUM')],
            [Markup.button.callback('Dato Curioso 🤯', 'OP_RANDOM_FACT')],
            [Markup.button.callback('Frase Random ✨', 'OP_RANDOM_PHRASE')],
            [Markup.button.callback('¿Qué puedes hacer? 🤖', 'OP_PUEDO')],
        ])
    );
});


// ---------------------------------
//  CUANDO EL USUARIO ENVÍA TEXTO
// ---------------------------------
bot.on('text', (ctx) => {
    ctx.reply(
        "Elige una opción 👇",
        Markup.inlineKeyboard([
            [Markup.button.callback('Saludar 👋', 'OP_HOLA')],
            [Markup.button.callback('¿Cómo estás? 🤔', 'OP_ESTAS')],
            [Markup.button.callback('Número Random 🔢', 'OP_RANDOM_NUM')],
            [Markup.button.callback('Dato Curioso 🤯', 'OP_RANDOM_FACT')],
            [Markup.button.callback('Frase Random ✨', 'OP_RANDOM_PHRASE')],
            [Markup.button.callback('¿Qué puedes hacer? 🤖', 'OP_PUEDO')],
        ])
    );
});


// ----------------------------
//   ACCIONES DE LOS BOTONES
// ----------------------------
bot.action('OP_HOLA', (ctx) => {
    ctx.answerCbQuery();
    ctx.reply("¡Hola! ¿Cómo estás? 😄");
});

bot.action('OP_ESTAS', (ctx) => {
    ctx.answerCbQuery();
    ctx.reply("Estoy funcionando al 100%, gracias por preguntar ⚡");
});


// 🔢 Número random
bot.action('OP_RANDOM_NUM', (ctx) => {
    ctx.answerCbQuery();
    const num = Math.floor(Math.random() * 1000) + 1;
    ctx.reply(`Tu número random es: *${num}* 🔢`, { parse_mode: 'Markdown' });
});


// 🤯 Dato curioso random
bot.action('OP_RANDOM_FACT', (ctx) => {
    ctx.answerCbQuery();

    const facts = [
        "Los pulpos tienen tres corazones 🐙",
        "El corazón humano puede latir hasta fuera del cuerpo ❤️",
        "Las abejas pueden reconocer rostros humanos 🐝",
        "Un día en Venus dura más que un año en Venus 🌌",
        "Los camellos tienen tres párpados para protegerse de la arena 🐪"
    ];

    const randomFact = facts[Math.floor(Math.random() * facts.length)];
    ctx.reply(`Dato curioso: ${randomFact}`);
});


// ✨ Frase random
bot.action('OP_RANDOM_PHRASE', (ctx) => {
    ctx.answerCbQuery();

    const phrases = [
        "La vida es 10% lo que te pasa y 90% cómo reaccionas.",
        "El éxito es la suma de pequeños esfuerzos repetidos diariamente.",
        "No cuentes los días, haz que los días cuenten.",
        "El único límite es tu mente.",
        "Hazlo con miedo, pero hazlo."
    ];

    const randomPhrase = phrases[Math.floor(Math.random() * phrases.length)];
    ctx.reply(`✨ ${randomPhrase}`);
});


// 🤖 ¿Qué puedes hacer?
bot.action('OP_PUEDO', (ctx) => {
    ctx.answerCbQuery();
    ctx.reply("Puedo enviarte datos random, saludarte y mucho más 🤖✨");
});


// ----------------------------
//      INICIAR BOT
// ----------------------------
bot.launch()
    .then(() => console.log("Bot iniciado correctamente 🚀"))
    .catch(err => console.error("Error al iniciar el bot:", err));

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
