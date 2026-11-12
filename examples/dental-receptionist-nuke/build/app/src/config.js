export const SLOT_MINUTES = 60;
export const OPEN_HOUR = 8;
export const CLOSE_HOUR = 17;
export const DEFAULT_PORT = 8080;
export const MAX_SLOTS_OFFERED = 3;

export function readConfig(env = process.env) {
  return {
    port: Number(env.PORT) || DEFAULT_PORT,
    retellApiKey: env.RETELL_API_KEY ?? '',
    developerKey: env.OPEN_DENTAL_DEVELOPER_KEY ?? '',
    customerKey: env.OPEN_DENTAL_CUSTOMER_KEY ?? '',
  };
}
