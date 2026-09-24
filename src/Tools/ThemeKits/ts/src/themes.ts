export const themeNames = ["light", "dark", "logistics", "future"] as const;
export type ThemeName = typeof themeNames[number];

export interface ThemeTarget {
    dataset: DOMStringMap;
}

export function isThemeName(value: string): value is ThemeName {
    return (themeNames as readonly string[]).includes(value);
}

export function applyTheme(theme: ThemeName, target: ThemeTarget = document.documentElement): void {
    target.dataset.saysolTheme = theme;
}

export function readTheme(target: ThemeTarget = document.documentElement): ThemeName | null {
    const value = target.dataset.saysolTheme;
    return value && isThemeName(value) ? value : null;
}
