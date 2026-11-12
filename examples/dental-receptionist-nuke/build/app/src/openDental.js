const BASE_URL = 'https://api.opendental.com/api/v1';

function headers(cfg) {
  return {
    Authorization: `ODFHIR ${cfg.developerKey}/${cfg.customerKey}`,
    'Content-Type': 'application/json',
  };
}

export async function listAppointments(cfg, date) {
  const res = await fetch(`${BASE_URL}/appointments?date=${date}`, { headers: headers(cfg) });
  if (!res.ok) throw new Error(`Open Dental list failed: ${res.status}`);
  return res.json();
}

export async function createAppointment(cfg, appointment) {
  const res = await fetch(`${BASE_URL}/appointments`, {
    method: 'POST',
    headers: headers(cfg),
    body: JSON.stringify(appointment),
  });
  if (!res.ok) throw new Error(`Open Dental create failed: ${res.status}`);
  return res.json();
}
