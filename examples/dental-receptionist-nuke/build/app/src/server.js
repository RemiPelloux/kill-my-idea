import { createServer } from 'node:http';
import { readConfig } from './config.js';
import { openSlots } from './slots.js';

const cfg = readConfig();

async function readJson(req) {
  let body = '';
  for await (const chunk of req) body += chunk;
  return body ? JSON.parse(body) : {};
}

function send(res, status, data) {
  res.writeHead(status, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(data));
}

const routes = {
  'POST /availability': async (body) => ({ slots: openSlots(new Date(body.date), []) }),
  'POST /handoff': async () => ({ action: 'transfer_to_front_desk' }),
};

createServer(async (req, res) => {
  const handler = routes[`${req.method} ${req.url}`];
  if (!handler) return send(res, 404, { error: 'not found' });
  try {
    send(res, 200, await handler(await readJson(req)));
  } catch (err) {
    send(res, 400, { error: err.message });
  }
}).listen(cfg.port, () => console.log(`LunchLine webhooks on :${cfg.port}`));
