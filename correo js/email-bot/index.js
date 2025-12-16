


// index.js
require('dotenv').config();
console.log("Variables cargadas:", process.env.SMTP_USER, process.env.TO_EMAIL);

const express = require('express');
const nodemailer = require('nodemailer');

const {
  SMTP_HOST,
  SMTP_PORT,
  SMTP_SECURE,
  SMTP_USER,
  SMTP_PASS,
  TO_EMAIL,
  FROM_NAME,
  FROM_EMAIL,
  PORT = 3000
} = process.env;

if (!SMTP_USER || !SMTP_PASS || !TO_EMAIL) {
  console.error('Faltan variables de entorno. Revisa .env (SMTP_USER, SMTP_PASS, TO_EMAIL).');
  process.exit(1);
}

const transporter = nodemailer.createTransport({
  host: SMTP_HOST || 'smtp.gmail.com',
  port: Number(SMTP_PORT) || 465,
  secure: (SMTP_SECURE === 'true') || true,
  auth: {
    user: SMTP_USER,
    pass: SMTP_PASS
  }
});

// Verificar conexión al servidor SMTP (opcional)
transporter.verify().then(() => {
  console.log('Conexión SMTP OK');
}).catch(err => {
  console.error('Error al verificar SMTP:', err.message);
});

const app = express();
app.use(express.json());

// Endpoint simple para disparar el correo
app.post('/send', async (req, res) => {
  try {
    const { subject = 'Prueba desde mi bot', text = 'Hola — este es un mensaje enviado por mi bot en Node.js' } = req.body || {};

    const mailOptions = {
      from: `"${FROM_NAME || 'Bot'}" <${FROM_EMAIL || SMTP_USER}>`,
      to: TO_EMAIL,
      subject,
      text,
      // html: '<b>Contenido en HTML</b>' // opcional
    };

    const info = await transporter.sendMail(mailOptions);
    console.log('Correo enviado:', info.messageId);
    res.json({ ok: true, messageId: info.messageId });
  } catch (err) {
    console.error('Error enviando correo:', err);
    res.status(500).json({ ok: false, error: err.message });
  }
});

// Opcional: endpoint para enviar a cualquier email (con precaución)
app.post('/send-to', async (req, res) => {
  try {
    const { to, subject = 'Mensaje desde bot', text = 'Contenido' } = req.body;
    if (!to) return res.status(400).json({ ok: false, error: 'Falta campo "to".' });

    const mailOptions = {
      from: `"${FROM_NAME || 'Bot'}" <${FROM_EMAIL || SMTP_USER}>`,
      to,
      subject,
      text
    };

    const info = await transporter.sendMail(mailOptions);
    res.json({ ok: true, messageId: info.messageId });
  } catch (err) {
    res.status(500).json({ ok: false, error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Email-bot escuchando en http://localhost:${PORT}`);
  console.log('POST /send para enviar el correo configurado en TO_EMAIL');
});
