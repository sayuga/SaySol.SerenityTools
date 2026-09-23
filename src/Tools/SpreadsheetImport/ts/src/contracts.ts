export type MappingStatus =
    | "mapped"
    | "unmapped"
    | "ambiguous"
    | "duplicate-target";

export interface ColumnMapping {
    columnIndex: number;
    header: string;
    fieldKey: string | null;
    status: MappingStatus;
    candidateFieldKeys: readonly string[];
}

export interface ImportIssue {
    code: string;
    message: string;
    rowNumber?: number;
    columnIndex?: number;
    fieldKey?: string;
}

export interface PreviewRow {
    rowNumber: number;
    values: Readonly<Record<string, unknown>>;
    issues: readonly ImportIssue[];
}

export interface ImportPreview {
    token: string;
    profileKey: string;
    fileSha256: string;
    mappings: readonly ColumnMapping[];
    rows: readonly PreviewRow[];
    issues: readonly ImportIssue[];
    expiresAtUtc: string;
}

export interface CommitResult {
    inserted: number;
    updated: number;
    skipped: number;
    issues: readonly ImportIssue[];
}

export interface SpreadsheetImportTransport {
    preview(profileKey: string, uploadToken: string): Promise<ImportPreview>;
    commit(previewToken: string, idempotencyKey: string): Promise<CommitResult>;
}
