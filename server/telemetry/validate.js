// A tiny JSON Schema check for the keywords report.schema.json uses. It mirrors validate() in
// skills/opendesigner/scripts/journey.py, so the sender and the receiver agree on what a report may hold.
export function validate(value, schema, root = schema, path = "$") {
  if (schema.$ref) {
    const node = schema.$ref.replace(/^#\//, "").split("/").reduce((n, part) => n[part], root);
    return validate(value, node, root, path);
  }
  const isNum = typeof value === "number" && Number.isFinite(value);
  const isObj = value !== null && typeof value === "object" && !Array.isArray(value);
  const types = { object: isObj, array: Array.isArray(value), string: typeof value === "string",
                  boolean: typeof value === "boolean", number: isNum, integer: isNum && Number.isInteger(value) };
  if (schema.type && !types[schema.type]) return [`${path}: expected ${schema.type}`];
  const errs = [];
  if ("const" in schema && value !== schema.const) errs.push(`${path}: must be ${JSON.stringify(schema.const)}`);
  if (schema.enum && !schema.enum.includes(value)) errs.push(`${path}: not an allowed value`);
  if (typeof value === "string") {
    if (schema.pattern && !new RegExp(schema.pattern).test(value)) errs.push(`${path}: does not match ${schema.pattern}`);
    if (schema.maxLength !== undefined && value.length > schema.maxLength) errs.push(`${path}: too long`);
  }
  if (isNum) {
    if ((schema.minimum !== undefined && value < schema.minimum) || (schema.maximum !== undefined && value > schema.maximum)) {
      errs.push(`${path}: out of range`);
    }
    if (schema.multipleOf && value % schema.multipleOf) errs.push(`${path}: not a multiple of ${schema.multipleOf}`);
  }
  if (Array.isArray(value)) {
    if (schema.maxItems !== undefined && value.length > schema.maxItems) errs.push(`${path}: too many items`);
    value.forEach((v, i) => errs.push(...validate(v, schema.items || {}, root, `${path}[${i}]`)));
  }
  if (isObj) {
    for (const k of schema.required || []) if (!(k in value)) errs.push(`${path}: missing ${k}`);
    const keys = Object.keys(value);
    if (schema.maxProperties !== undefined && keys.length > schema.maxProperties) errs.push(`${path}: too many keys`);
    const props = schema.properties || {};
    const extra = schema.additionalProperties === undefined ? true : schema.additionalProperties;
    for (const k of keys) {
      if (schema.propertyNames) errs.push(...validate(k, schema.propertyNames, root, `${path}.<key ${k}>`));
      if (Object.hasOwn(props, k)) errs.push(...validate(value[k], props[k], root, `${path}.${k}`));
      else if (extra === false) errs.push(`${path}: key ${JSON.stringify(k)} is not allowed`);
      else if (typeof extra === "object") errs.push(...validate(value[k], extra, root, `${path}.${k}`));
    }
  }
  return errs;
}
