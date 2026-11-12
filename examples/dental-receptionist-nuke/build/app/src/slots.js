import { SLOT_MINUTES, OPEN_HOUR, CLOSE_HOUR, MAX_SLOTS_OFFERED } from './config.js';

const MINUTE_MS = 60_000;

export function overlaps(start, end, appt) {
  return start < appt.end && appt.start < end;
}

export function candidateSlots(day) {
  const slots = [];
  for (let h = OPEN_HOUR; h < CLOSE_HOUR; h += SLOT_MINUTES / 60) {
    const start = new Date(day);
    start.setHours(h, 0, 0, 0);
    slots.push({ start, end: new Date(start.getTime() + SLOT_MINUTES * MINUTE_MS) });
  }
  return slots;
}

export function openSlots(day, appointments, limit = MAX_SLOTS_OFFERED) {
  return candidateSlots(day)
    .filter((s) => !appointments.some((a) => overlaps(s.start, s.end, a)))
    .slice(0, limit);
}
