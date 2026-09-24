export type WidgetTone = "neutral" | "primary" | "success" | "warning" | "danger";

export interface WidgetAction {
    label: string;
    href?: string;
    onActivate?: () => void;
}

export interface InfoCardOptions {
    label: string;
    value: string;
    detail?: string;
    iconLabel?: string;
    tone?: WidgetTone;
    progress?: number;
    action?: WidgetAction;
}

export interface PanelOptions {
    title: string;
    content: Node | string;
    tone?: WidgetTone;
    collapsible?: boolean;
    initiallyCollapsed?: boolean;
}

function element<K extends keyof HTMLElementTagNameMap>(
    tag: K,
    className?: string,
    text?: string
): HTMLElementTagNameMap[K] {
    const result = document.createElement(tag);
    if (className)
        result.className = className;
    if (text !== undefined)
        result.textContent = text;
    return result;
}

function toneClass(tone: WidgetTone | undefined): string {
    return `saysol-tone-${tone ?? "neutral"}`;
}

function appendAction(parent: HTMLElement, action: WidgetAction): void {
    const control = action.href
        ? element("a", "saysol-widget__action", action.label)
        : element("button", "saysol-widget__action", action.label);
    if (control instanceof HTMLAnchorElement)
        control.href = action.href!;
    else
        control.type = "button";
    if (action.onActivate)
        control.addEventListener("click", action.onActivate);
    parent.append(control);
}

export function createInfoCard(options: InfoCardOptions): HTMLElement {
    const card = element("section", `saysol-widget saysol-info-card ${toneClass(options.tone)}`);
    card.setAttribute("aria-label", options.label);
    if (options.iconLabel) {
        const icon = element("span", "saysol-info-card__icon", options.iconLabel);
        icon.setAttribute("aria-hidden", "true");
        card.append(icon);
    }
    const content = element("div", "saysol-info-card__content");
    content.append(
        element("span", "saysol-info-card__label", options.label),
        element("strong", "saysol-info-card__value", options.value)
    );
    if (options.progress !== undefined) {
        const progress = element("progress", "saysol-info-card__progress");
        progress.max = 100;
        progress.value = Math.max(0, Math.min(100, options.progress));
        progress.setAttribute("aria-label", `${options.label} progress`);
        content.append(progress);
    }
    if (options.detail)
        content.append(element("span", "saysol-info-card__detail", options.detail));
    if (options.action)
        appendAction(content, options.action);
    card.append(content);
    return card;
}

export function createStatCard(options: InfoCardOptions): HTMLElement {
    const card = createInfoCard(options);
    card.classList.add("saysol-stat-card");
    return card;
}

export function createPanel(options: PanelOptions): HTMLElement {
    const panel = element("section", `saysol-widget saysol-panel ${toneClass(options.tone)}`);
    const heading = element("header", "saysol-panel__header");
    heading.append(element("h2", "saysol-panel__title", options.title));
    const body = element("div", "saysol-panel__body");
    body.append(typeof options.content === "string"
        ? document.createTextNode(options.content)
        : options.content);
    if (options.collapsible) {
        const button = element("button", "saysol-panel__toggle", "Toggle");
        button.type = "button";
        button.setAttribute("aria-expanded", String(!options.initiallyCollapsed));
        body.hidden = options.initiallyCollapsed ?? false;
        button.addEventListener("click", () => {
            body.hidden = !body.hidden;
            button.setAttribute("aria-expanded", String(!body.hidden));
        });
        heading.append(button);
    }
    panel.append(heading, body);
    return panel;
}

export function createEmptyState(title: string, detail?: string): HTMLElement {
    const state = element("section", "saysol-widget saysol-empty-state");
    state.append(element("h2", "saysol-empty-state__title", title));
    if (detail)
        state.append(element("p", "saysol-empty-state__detail", detail));
    return state;
}
