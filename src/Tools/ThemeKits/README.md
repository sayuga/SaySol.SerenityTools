# Theme Kits capsule

Version: 0.1.0  
Maturity: implemented TypeScript/CSS core; not Serenity-host verified

Theme Kits supplies semantic design tokens and four initial visual kits: Light,
Dark, Logistics, and Future. Themes are applied through a stable
`data-saysol-theme` attribute and CSS custom properties, keeping host components
and the Widget Library independent from hard-coded palette classes.

The core does not replace Serenity layout markup, inject HTML, or store a user's
selection. Host integration must decide whether selection is fixed, per-user,
or centrally configured and must avoid a flash of the wrong theme during load.

No code has been promoted to `Serenity.SaySolShared`; this capsule is the sole
owner of theme selection today.
