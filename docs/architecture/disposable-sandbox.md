# Disposable sandbox architecture

The approved baseline is an immutable Git tag. A working instance is a copy
created by the bounded instantiate script; capsule installers mutate only that
copy. Evidence is preserved outside it before disposal.

Promotion requires dependency update, regeneration review, clean validation,
regression of verified capsules, review, and explicit owner approval. Only then
may an owner create sandbox/v-baseline-serenity-version and set the manifest to
approved. CI never advances pins or creates approval tags.

Capsule evidence is invalid unless the same fresh host first recorded a clean
baseline PASS.
