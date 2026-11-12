import { test } from 'node:test';
import assert from 'node:assert/strict';
import { openSlots, overlaps } from '../src/slots.js';

const day = new Date('2026-12-01T00:00:00');
const at = (h) => { const d = new Date(day); d.setHours(h, 0, 0, 0); return d; };

test('overlaps detects intersecting ranges', () => {
  assert.equal(overlaps(at(9), at(10), { start: at(9), end: at(10) }), true);
  assert.equal(overlaps(at(9), at(10), { start: at(10), end: at(11) }), false);
});

test('openSlots skips booked hours and caps the offer', () => {
  const slots = openSlots(day, [{ start: at(8), end: at(10) }]);
  assert.equal(slots.length, 3);
  assert.equal(slots[0].start.getHours(), 10);
});
