# Browser Automation Recipes — Extended

Neutral, widely-used techniques for reliably filling forms in a CDP-driven browser
(Playwright / Puppeteer / equivalent). These are general web-automation patterns, not
circumvention techniques.

## 1. Set input values so framework state updates
Assigning `.value` directly is ignored by React/Vue. Use the native setter + events:

```js
const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
set.call(el, value);
el.dispatchEvent(new Event('input',  { bubbles: true }));
el.dispatchEvent(new Event('change', { bubbles: true }));
```

- Use `HTMLTextAreaElement.prototype` for textareas.
- Use `HTMLSelectElement.prototype` for selects.
- Checkboxes/radios: set `.checked` then dispatch `click` or `change`.

## 2. Scope selectors to the form
Bare `[name=description]` can collide with `<meta name="description">`.

```js
document.querySelector('form [name=description]')
```

## 3. Custom comboboxes (react-select v1 pattern)
1. Open the menu with `mousedown` on `.Select-control`.
2. Dispatch `mousedown` → `mouseup` → `click` on the `[role=option]` element.
3. Verify the selection in the visible `.Select-value-label`.
4. Note: the hidden `input.value` stays empty by design — do not assert on it.

## 4. iframes
- Get the frame list, then operate inside a frame with its `frameID`.
- Accessibility trees inside frames may be minimal — evaluate the DOM directly.
- **Cross-origin frames cannot be scripted.** That is the captcha wall. Stop and hand off to a human;
  do not attempt to defeat it.

## 5. Snapshot refs rotate
- Re-snapshot after every DOM mutation; stale refs fail silently.
- Scroll the target into view before clicking; some UIs require a "trusted" click path
  (`scrollIntoView` then a real click on a resolved ref).

## 6. Two-step signups & honeypots
- Some step-2 forms reject submissions that echo hidden/duplicate fields (title, name, content).
  Submit only `csrf + email + password + required`.
- Leave obvious honeypot fields (hidden inputs, duplicated confirm fields) empty.
- If a submit silently 403s, suspect honeypot echo fields.

## 7. Verification email handling
- Read the owner's inbox via the approved API and extract the confirmation link or code.
- Prefer the owner's real mailbox over relay domains — relays often silently drop.
- If the HTML body is returned as an object/array, parse the plain-text body instead of regexing HTML.
- Handle single-use tokens: do not burn them with repeated navigations.

## 8. Open publishing APIs
- Some platforms allow publishing with no account via an open API.
- Watch for strict content format requirements (e.g. structured node arrays with explicit anchor
  objects — plain strings may fail).
- Respect rate limits; on a cooldown error, retry sequentially with a delay.

## 9. General reliability
- Wait for load/network-idle between steps where the tool supports it.
- Re-read the page state after every submit; capture the confirmation ID from the resulting URL or DOM.
- Lower request rate on any WAF response; never escalate.
