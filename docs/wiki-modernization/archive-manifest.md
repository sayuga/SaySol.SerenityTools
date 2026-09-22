# Archived wiki manifest

Source: [serenity-is/Serenity wiki archive](https://github.com/serenity-is/Serenity/tree/master/wiki-archive)  
Source commit: `1c00f72c177fd7410c9f17d992f4d60115b0163a`  
Reviewed: 2026-09-22

This census covers all 141 files currently stored under `wiki-archive/`. Every
page has been located and assigned an initial functional category and disposition.
A `triaged` review status means the article has been identified and screened for
obvious legacy indicators; it does not yet claim current compatibility or a
successful build.

## Disposition counts

- `archive-obsolete`: 5
- `modernize-candidate`: 86
- `modernize-priority`: 1
- `reject-placeholder`: 10
- `replace-native`: 2
- `replace-official-docs`: 25
- `research-harden`: 12

## Status vocabulary

- `replace-official-docs`: preserve the topic pointer; use version-matched official documentation.
- `replace-native`: document the current Serenity-native implementation.
- `modernize-priority`: actively selected for a current reusable integration.
- `modernize-candidate`: potentially useful; current source/API review remains.
- `research-harden`: valuable but security, data integrity, concurrency, or operational design must precede implementation.
- `archive-obsolete`: tied to retired framework, browser, UI, or build patterns.
- `reject-placeholder`: no substantive implementation to recover.

## Complete archive census

| ID | Source file | Category | Lines | Disposition | Review status |
| --- | --- | --- | ---: | --- | --- |
| ARC-001 | `A-simple-notification-with-SignalR-in-Serene-StartSharp-(.NET-Core-version).md` | messaging-background | 272 | modernize-candidate | triaged |
| ARC-002 | `Additional-Feature-Implementing-Large-File-Upload-Editor.md` | files-storage | 46 | research-harden | triaged |
| ARC-003 | `Additional-Feature-Implementing-isCloneMode.md` | application-patterns | 94 | modernize-candidate | triaged |
| ARC-004 | `Additional-Feature-Implementing-server-side-IsInRole-and-client-side-hasRole.md` | security-audit | 230 | research-harden | triaged |
| ARC-005 | `Additional-Feature-Using-a-LookupEditor-in-direct-entry-in-a-Grid.md` | lookups | 132 | modernize-candidate | triaged |
| ARC-006 | `Audit-Details-in-the-XYZ-form-as-Master-Detail-relation.md` | security-audit | 332 | research-harden | triaged |
| ARC-007 | `Auditing-Audit-Log-for-Insert-Update-and-Delete-using-Single-Table.md` | security-audit | 397 | research-harden | triaged |
| ARC-008 | `Background-Tasks-Bulk-Email-Sending.md` | messaging-background | 260 | research-harden | triaged |
| ARC-009 | `Background-Tasks-Using-Hangfire-Background-Jobs.md` | messaging-background | 215 | research-harden | triaged |
| ARC-010 | `Change-Startup-page.md` | ui-dialogs-navigation | 14 | modernize-candidate | triaged |
| ARC-011 | `CheckBox-Group-Editor.md` | editors | 214 | modernize-candidate | triaged |
| ARC-012 | `ColorPickerEditor-by-Estrusco.md` | editors | 1 | reject-placeholder | triaged |
| ARC-013 | `Conditionally-disable-the-EditLinks-in-a-Detail-Editor-that-is-part-of--MasterDialog-with-a--Parent-Child-Relationship.md` | editors | 180 | modernize-candidate | triaged |
| ARC-014 | `Create-Bootstrap-3-Popover-Button-On-Serenity-Form.md` | ui-dialogs-navigation | 13 | archive-obsolete | triaged |
| ARC-015 | `Create-toolbar-dropdown-button.md` | ui-dialogs-navigation | 12 | modernize-candidate | triaged |
| ARC-016 | `Customize-RowLookupScript.md` | lookups | 9 | modernize-candidate | triaged |
| ARC-017 | `Database-Multi-Database-Serenity.md` | data-database | 184 | research-harden | triaged |
| ARC-018 | `Database-MySQL-Connection-Timeout-on-Northwind-Database-creation-during-site-initialization.md` | data-database | 27 | modernize-candidate | triaged |
| ARC-019 | `Database-One-application-with-different-database-per-customer.md` | data-database | 61 | research-harden | triaged |
| ARC-020 | `Database-Optimistic-locking-support-for-MS-SQL-Server-by-hannesb.md` | data-database | 193 | research-harden | triaged |
| ARC-021 | `Define-page-which-is-automatically-loaded-after-successful-login-dynamically-from-server-side.md` | application-patterns | 106 | modernize-candidate | triaged |
| ARC-022 | `Dialog-Cascading-windows.md` | ui-dialogs-navigation | 32 | modernize-candidate | triaged |
| ARC-023 | `Dialog-CloneableEntityDialog.md` | ui-dialogs-navigation | 1 | reject-placeholder | triaged |
| ARC-024 | `Dialog-Decorate-the-dialog's-title-with-HTML.md` | ui-dialogs-navigation | 37 | modernize-candidate | triaged |
| ARC-025 | `Dialog-add-copy-link-and-open-in-a-new-tab-buttons--Copied-From-#2104.md` | ui-dialogs-navigation | 203 | modernize-candidate | triaged |
| ARC-026 | `Editors-Autocomplete-Editor.md` | editors | 184 | modernize-candidate | triaged |
| ARC-027 | `Editors-Editor-Types.md` | editors | 211 | modernize-candidate | triaged |
| ARC-028 | `Editors-Signature-Editor-using-SignaturePad.md` | editors | 90 | modernize-candidate | triaged |
| ARC-029 | `Enable-CORS-For-Serenity-Applications.md` | security-audit | 31 | research-harden | triaged |
| ARC-030 | `Entity-Framework-AutoIncrementAttribute-[Mapping].md` | framework-reference | 21 | replace-official-docs | triaged |
| ARC-031 | `Entity-Framework-CalculatedAttribute-[Mapping].md` | framework-reference | 21 | replace-official-docs | triaged |
| ARC-032 | `Entity-Framework-ClientSideAttribute-[Mapping].md` | framework-reference | 25 | replace-official-docs | triaged |
| ARC-033 | `Entity-Framework-ColumnAttribute-[Mapping].md` | framework-reference | 57 | replace-official-docs | triaged |
| ARC-034 | `Entity-Framework-ConnectionKeyAttribute-[Mapping].md` | framework-reference | 19 | replace-official-docs | triaged |
| ARC-035 | `Entity-Framework-DatabaseAliasAttribute-[Mapping].md` | framework-reference | 11 | replace-official-docs | triaged |
| ARC-036 | `Entity-Framework-ExpressionAttribute-[Mapping].md` | framework-reference | 45 | replace-official-docs | triaged |
| ARC-037 | `Entity-Framework-FieldFlags-Enumeration.md` | framework-reference | 1 | reject-placeholder | triaged |
| ARC-038 | `Entity-Framework-ForeignKeyAttribute-[Mapping].md` | framework-reference | 26 | replace-official-docs | triaged |
| ARC-039 | `Entity-Framework-IdentityAttribute-[Mapping].md` | framework-reference | 16 | replace-official-docs | triaged |
| ARC-040 | `Entity-Framework-InsertableAttribute-[Common].md` | framework-reference | 31 | replace-official-docs | triaged |
| ARC-041 | `Entity-Framework-LeftJoinAttribute-[Mapping].md` | framework-reference | 195 | replace-official-docs | triaged |
| ARC-042 | `Entity-Framework-LinkingSetRelationAttribute-[Mapping].md` | framework-reference | 24 | replace-official-docs | triaged |
| ARC-043 | `Entity-Framework-LookupEditorAttribute-[PropertyGrid].md` | framework-reference | 45 | replace-official-docs | triaged |
| ARC-044 | `Entity-Framework-LookupIncludeAttribute-[Mapping].md` | framework-reference | 41 | replace-official-docs | triaged |
| ARC-045 | `Entity-Framework-LookupScriptAttribute-[Extensibility].md` | framework-reference | 51 | replace-official-docs | triaged |
| ARC-046 | `Entity-Framework-NotNullAttribute-[Mapping].md` | framework-reference | 20 | replace-official-docs | triaged |
| ARC-047 | `Entity-Framework-PrimaryKeyAttribute-[Mapping].md` | framework-reference | 24 | replace-official-docs | triaged |
| ARC-048 | `Entity-Framework-ReadOnlyAttribute-[Common].md` | framework-reference | 16 | replace-official-docs | triaged |
| ARC-049 | `Entity-Framework-SetFieldFlagsAttribute-[Mapping].md` | framework-reference | 46 | replace-official-docs | triaged |
| ARC-050 | `Entity-Framework-TableNameAttribute-[Mapping].md` | framework-reference | 49 | replace-official-docs | triaged |
| ARC-051 | `Entity-Framework-UniqueAttribute-[Mapping].md` | framework-reference | 20 | replace-official-docs | triaged |
| ARC-052 | `Entity-Framework-UpdatableAttribute-[Common].md` | framework-reference | 30 | replace-official-docs | triaged |
| ARC-053 | `Excel-Import-Extended---Column-Mapping-and-Import-Value-Type-Handling.md` | import-export-reporting | 242 | modernize-priority | triaged |
| ARC-054 | `File-Download-at-click-on-button.md` | files-storage | 86 | modernize-candidate | triaged |
| ARC-055 | `FileUploadEditor-Confirmation.md` | files-storage | 40 | modernize-candidate | triaged |
| ARC-056 | `Fix-Blank-Login-Page-After-Publishing-to-Web-Server--Uncaught-ReferenceError-jQuery-is-not-defined.md` | tooling-troubleshooting | 8 | modernize-candidate | triaged |
| ARC-057 | `Fix-Language-Selection-does-not-work-in-IE11-and-recent-Serenity-Frameworks.md` | tooling-troubleshooting | 59 | archive-obsolete | triaged |
| ARC-058 | `Fix-grid-frozenColumn-and-sidebar-toogle.md` | grids | 35 | modernize-candidate | triaged |
| ARC-059 | `Formatting-AlignCenterAttribute-[Columns].md` | ui-dialogs-navigation | 28 | modernize-candidate | triaged |
| ARC-060 | `Formatting-AlignRightAttribute-[Columns].md` | ui-dialogs-navigation | 28 | modernize-candidate | triaged |
| ARC-061 | `Forms-Create-another-form-of-the-same-Sergen-generated-table.md` | ui-dialogs-navigation | 75 | modernize-candidate | triaged |
| ARC-062 | `Forms-Tab-order-on-serenity-form.md` | ui-dialogs-navigation | 21 | modernize-candidate | triaged |
| ARC-063 | `Frequently-Asked-Questions.md` | application-patterns | 99 | replace-official-docs | triaged |
| ARC-064 | `Get-Inserted-Record-ID.md` | application-patterns | 1 | reject-placeholder | triaged |
| ARC-065 | `Grid---Mixin---Custom-grid-pager-without-counting-total-records.md` | grids | 281 | modernize-candidate | triaged |
| ARC-066 | `Grid-Adding-Active-Delete-(Delete-Undelete)-to-a-Grid.md` | grids | 75 | modernize-candidate | triaged |
| ARC-067 | `Grid-Defining-a-Sort-Order..md` | grids | 17 | modernize-candidate | triaged |
| ARC-068 | `Grid-EditLinkAttribute-[Columns].md` | grids | 49 | modernize-candidate | triaged |
| ARC-069 | `Grid-LookupFilteringAttribute-[Columns].md` | lookups | 71 | modernize-candidate | triaged |
| ARC-070 | `Grid-Make-detail-grid-in-Master-Detail-sortable.md` | grids | 73 | modernize-candidate | triaged |
| ARC-071 | `Grid-Radio-Row-Selection-Mixin.md` | grids | 36 | modernize-candidate | triaged |
| ARC-072 | `Grid-Refresh-Grid-from-open-Dialog.md` | grids | 16 | modernize-candidate | triaged |
| ARC-073 | `Grid-SlickGrid-Column-Picker-(by-marcobisio).md` | grids | 48 | modernize-candidate | triaged |
| ARC-074 | `Grid-SlickGrid-Formatters.md` | grids | 199 | modernize-candidate | triaged |
| ARC-075 | `Grid-Slickgrid-AutoColumn-resize.md` | grids | 238 | modernize-candidate | triaged |
| ARC-076 | `Grid-WidthAttribute-[Columns].md` | grids | 30 | modernize-candidate | triaged |
| ARC-077 | `Group-notifications-with-SignalR-(by-marcobisio).md` | messaging-background | 276 | modernize-candidate | triaged |
| ARC-078 | `How-to-fix-Javascript-Intellisense-in-cshtml.md` | tooling-troubleshooting | 16 | modernize-candidate | triaged |
| ARC-079 | `Issue-Guidelines.md` | application-patterns | 36 | modernize-candidate | triaged |
| ARC-080 | `JQuery-Autocomplete.md` | application-patterns | 168 | archive-obsolete | triaged |
| ARC-081 | `LinkingSetRelation-Explanation.md` | application-patterns | 52 | modernize-candidate | triaged |
| ARC-082 | `Localization-(SF-only-solution)-Transparently-localize-content-and-fall-back-to-standard-value-when-no-localization-in-selected-UI-language-is-available.md` | application-patterns | 197 | modernize-candidate | triaged |
| ARC-083 | `Lookup-Editors-How-to-Create-Lookup-Editor-for-code-description-tables.md` | lookups | 185 | modernize-candidate | triaged |
| ARC-084 | `Lookups-Refresh-Lookups-on-TypeScript.md` | lookups | 16 | modernize-candidate | triaged |
| ARC-085 | `Lookups-RowLookupScript.md` | lookups | 101 | modernize-candidate | triaged |
| ARC-086 | `Lookups.md` | lookups | 14 | modernize-candidate | triaged |
| ARC-087 | `Methodic-How-To-VR-Architect's-How-To-List.md` | application-patterns | 88 | modernize-candidate | triaged |
| ARC-088 | `Notifications-Email-After-Inserting-or-Updating.md` | messaging-background | 123 | research-harden | triaged |
| ARC-089 | `Pascal-Case-Handling-in-Postgresql.md` | data-database | 21 | modernize-candidate | triaged |
| ARC-090 | `ReadOnlyAttribute-[Common].md` | application-patterns | 1 | reject-placeholder | triaged |
| ARC-091 | `Realtime-Group-notifications-with-SignalR-(by-marcobisio).md` | messaging-background | 276 | modernize-candidate | triaged |
| ARC-092 | `Reporting-Adding-CSV-Export.md` | import-export-reporting | 409 | modernize-candidate | triaged |
| ARC-093 | `Reporting-Adding-Excel-Export.md` | import-export-reporting | 67 | replace-native | triaged |
| ARC-094 | `Reporting-Adding-PDF-Export.md` | import-export-reporting | 68 | replace-native | triaged |
| ARC-095 | `Reporting-How-to-add-Header-and-Footer-in-WKHTMLTOPDF-report.md` | import-export-reporting | 99 | archive-obsolete | triaged |
| ARC-096 | `Reporting-Integrating-Telerik-Reporting.md` | import-export-reporting | 271 | modernize-candidate | triaged |
| ARC-097 | `Security-Preventing-CSRF-attacks-(Implementing-AntiForgery).md` | security-audit | 93 | research-harden | triaged |
| ARC-098 | `Serenity-Framework-Attributes.md` | framework-reference | 184 | replace-official-docs | triaged |
| ARC-099 | `Serenity-LookupEditor---Pass-Parameter-And-Change-LookupKey.md` | lookups | 147 | modernize-candidate | triaged |
| ARC-100 | `Server-Side-Cache-Invalidate-Lookup-Script.md` | lookups | 51 | modernize-candidate | triaged |
| ARC-101 | `Set-Default-Values-In-New-Dialog.md` | ui-dialogs-navigation | 1 | reject-placeholder | triaged |
| ARC-102 | `Set-Default-Values-Loading-default-data-in-a-PropertyPanel-with-form.md` | ui-dialogs-navigation | 18 | modernize-candidate | triaged |
| ARC-103 | `Setting-value-on-XYZ-form-from-database-retrieve-in-select2-dropdown.event.md` | data-database | 45 | modernize-candidate | triaged |
| ARC-104 | `SignaturePad-100%-Pure-Beef-TypeScript-Implementation.md` | editors | 953 | modernize-candidate | triaged |
| ARC-105 | `SlickGrid-Formatters.md` | grids | 1 | reject-placeholder | triaged |
| ARC-106 | `The-Wonder-of-Q.md` | application-patterns | 16 | archive-obsolete | triaged |
| ARC-107 | `Troubleshooting.md` | tooling-troubleshooting | 194 | replace-official-docs | triaged |
| ARC-108 | `UI-Bootstrap-Material-Design-Switch.md` | ui-dialogs-navigation | 170 | modernize-candidate | triaged |
| ARC-109 | `UI-Bootstrap-Switch-plugin-(by-marcobisio).md` | ui-dialogs-navigation | 89 | modernize-candidate | triaged |
| ARC-110 | `UI-Buttons-Use-FontAwesome-icons-instead-of-bitmaps.md` | ui-dialogs-navigation | 30 | modernize-candidate | triaged |
| ARC-111 | `UI-CSSResponsiveness.md` | ui-dialogs-navigation | 3 | reject-placeholder | triaged |
| ARC-112 | `UI-Chart-in-dialog.md` | ui-dialogs-navigation | 1 | reject-placeholder | triaged |
| ARC-113 | `UI-ColorPickerEditor-by-Estrusco.md` | editors | 71 | modernize-candidate | triaged |
| ARC-114 | `UI-Custom-HTML-in-dialog.md` | ui-dialogs-navigation | 62 | modernize-candidate | triaged |
| ARC-115 | `UI-Customizing-the-Login-Screen.md` | ui-dialogs-navigation | 400 | modernize-candidate | triaged |
| ARC-116 | `UI-Customizing-the-UI--Icons.md` | ui-dialogs-navigation | 13 | modernize-candidate | triaged |
| ARC-117 | `UI-DialogMessages-and-DialogBoxes.md` | ui-dialogs-navigation | 1 | reject-placeholder | triaged |
| ARC-118 | `UI-Dynamic-navigation-items.md` | ui-dialogs-navigation | 99 | modernize-candidate | triaged |
| ARC-119 | `UI-EnableDisableControls.md` | ui-dialogs-navigation | 69 | modernize-candidate | triaged |
| ARC-120 | `UI-Form-and-Dialog.md` | ui-dialogs-navigation | 11 | modernize-candidate | triaged |
| ARC-121 | `UI-HiddenAttribute-[Common].md` | ui-dialogs-navigation | 45 | modernize-candidate | triaged |
| ARC-122 | `UI-Hide-Form-Categories-then-Show-on-Field-Trigger.md` | ui-dialogs-navigation | 48 | modernize-candidate | triaged |
| ARC-123 | `UI-HideOnInsertAttribute-[Common].md` | ui-dialogs-navigation | 20 | modernize-candidate | triaged |
| ARC-124 | `UI-HideOnUpdateAttribute-[Common].md` | ui-dialogs-navigation | 20 | modernize-candidate | triaged |
| ARC-125 | `UI-HtmlCodeEditor-using-CodeMirror.md` | editors | 108 | modernize-candidate | triaged |
| ARC-126 | `UI-Inserting-divider-lines-after-individual-top-level-menu-entries-on-the-left-navigation-bar.md` | ui-dialogs-navigation | 54 | modernize-candidate | triaged |
| ARC-127 | `UI-Layout-Improvements-[Notification-Icons-&-User-Personalization].md` | ui-dialogs-navigation | 131 | modernize-candidate | triaged |
| ARC-128 | `UI-Make-Grid-Fullsize.md` | grids | 66 | modernize-candidate | triaged |
| ARC-129 | `UI-Master-Detail-dialog;-Set-the-height-of-detail-grid.md` | grids | 31 | modernize-candidate | triaged |
| ARC-130 | `UI-Quickfilter-dropdown-show-colors-instead-of-text.md` | ui-dialogs-navigation | 79 | modernize-candidate | triaged |
| ARC-131 | `UI-Remove-changing-backgrounds-on-Login-page.md` | ui-dialogs-navigation | 51 | modernize-candidate | triaged |
| ARC-132 | `UI-Set-form-fields-label-(caption)-programmatically-without-losing-is-required-handling.md` | ui-dialogs-navigation | 27 | modernize-candidate | triaged |
| ARC-133 | `UI-Show-hide-programmatically-a-message-below-a-field-in-a-dialog.md` | ui-dialogs-navigation | 8 | modernize-candidate | triaged |
| ARC-134 | `UI-Slider-dialog-(poor-mans-EntityGridDialog).md` | grids | 460 | modernize-candidate | triaged |
| ARC-135 | `UI-SplitButton-dropdowns.md` | ui-dialogs-navigation | 112 | modernize-candidate | triaged |
| ARC-136 | `UI-Toolbar-Button-handling.md` | ui-dialogs-navigation | 48 | modernize-candidate | triaged |
| ARC-137 | `UI-User-image-at-login.md` | ui-dialogs-navigation | 140 | modernize-candidate | triaged |
| ARC-138 | `UI-VisibleAttribute-[Common].md` | ui-dialogs-navigation | 43 | modernize-candidate | triaged |
| ARC-139 | `Utils-ReadOnly-Binding-Utils.md` | application-patterns | 33 | modernize-candidate | triaged |
| ARC-140 | `Visual-Studio-Workaround-for-locked-files-when-trying-to-build.md` | tooling-troubleshooting | 23 | modernize-candidate | triaged |
| ARC-141 | `[BBB]-On-client-side-fetching-a-value-from-server-side-out-of-database.md` | data-database | 228 | modernize-candidate | triaged |
