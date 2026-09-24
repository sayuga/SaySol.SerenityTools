# Wiki source and publishing

This directory is the version-controlled source for the SaySol SerenityTools
GitHub Wiki. Changes are reviewed, tested, and committed with the capsule code
they describe. The rendered GitHub Wiki is a publication target, not the sole
copy of the documentation.

## Page policy

- Create a detailed page when a tool reaches design, recipe, or implementation.
- Do not publish empty pages for planned groupings.
- Match maturity and compatibility to `catalog.yaml` and `capsule.yaml`.
- Register each page in `tool-pages.yaml`, including documentation/tool version,
  exact compatibility lanes, evidence level, installation state, and test state.
- Include source provenance, scope, dependencies, security, installation,
  validation evidence, upgrade, and uninstall.
- Use `Tool-Page-Template.md` as the starting structure.
- Never document a host mutation that is absent from the capsule manifest.

## GitHub Wiki publication

GitHub stores the Wiki in the separate repository
`sayuga/SaySol.SerenityTools.wiki.git`. A maintainer with authenticated GitHub
Git access can clone that repository, copy the publishable Markdown pages from
this directory, review the diff, and push it. `README.md` and
`Tool-Page-Template.md` are maintenance sources and need not appear in the
rendered Wiki.

Automated publication should be added only with a narrowly scoped credential,
source/target diff reporting, and no ability to modify the main code repository.
