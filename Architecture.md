# 🏗️ Frontend Architecture Documentation

## Overview

This document explains the technical architecture, design decisions, and component structure of the AI Health Chatbot frontend.

---

## Technology Stack

### Core
- **React 18.2** - UI framework
- **Vite 5.0** - Build tool and dev server
- **Tailwind CSS 3.4** - Utility-first styling
- **Axios 1.6** - HTTP client

### Supporting
- **Lucide React** - Icon library
- **PostCSS** - CSS processing
- **Context API** - State management (theme)

### Why These Choices?

**React** - Component-based, large ecosystem, excellent performance
**Vite** - 10x faster than CRA, better DX, optimized builds
**Tailwind** - Rapid development, consistent design, tree-shakeable
**Axios** - Better error handling than fetch, interceptors, timeouts

---

## Project Structure

```
src/
├── components/           # React components
│   ├── Header.jsx        # Top bar with branding
│   ├── ChatWindow.jsx    # Message container
│   ├── MessageBubble.jsx # Individual message
│   ├── InputBox.jsx      # User input
│   ├── TypingIndicator.jsx # Bot typing animation
│   ├── ErrorMessage.jsx  # Error display
│   └── WelcomeScreen.jsx # Initial screen
├── context/
│   └── ThemeContext.jsx  # Dark mode state
├── services/
│   └── api.js            # Backend integration
├── App.jsx               # Main orchestrator
├── main.jsx              # React entry point
└── index.css             # Global styles
```

### Design Principles

1. **Single Responsibility** - Each component does one thing
2. **Composition over Inheritance** - Build complex UIs from simple pieces
3. **Props Down, Events Up** - Unidirectional data flow
4. **Minimal State** - State lives at the appropriate level
5. **Reusability** - Components work in different contexts

---

## Component Architecture

### App.jsx (Root)
**Responsibility**: State management and orchestration

**State**:
- `messages` - Array of all chat messages
- `isTyping` - Boolean for typing indicator
- `error` - Current error message (if any)
- `lastUserMessage` - For retry functionality

**Data Flow**:
```
User Input → handleSendMessage → API Call → Update State → Re-render
```

**Why at root?** 
- All components need access to messages
- Single source of truth for chat state
- Easier to debug and test

### ChatWindow.jsx
**Responsibility**: Display messages with auto-scroll

**Features**:
- Auto-scroll to latest message
- Conditional rendering (empty state vs messages)
- Smooth animations on new messages

**Technical Details**:
- Uses `useRef` for scroll anchor
- `useEffect` triggers scroll on message changes
- Custom scrollbar styling

### MessageBubble.jsx
**Responsibility**: Render individual message

**Props**:
- `message` - Object with text, sender, timestamp
- `isBot` - Boolean for styling

**Styling Logic**:
- User messages: right-aligned, blue gradient
- Bot messages: left-aligned, white/gray
- Avatar icons: different for user/bot

### InputBox.jsx
**Responsibility**: Handle user input and submission

**Features**:
- Auto-resize textarea (up to 4 lines)
- Enter to send, Shift+Enter for newline
- Character counter
- Disabled state while bot responds

**UX Details**:
- Loading spinner on send button
- Keyboard shortcuts visible
- Visual feedback on focus

### TypingIndicator.jsx
**Responsibility**: Show bot is "thinking"

**Implementation**:
- 3 animated dots
- CSS keyframe animation
- Staggered animation delays

### ErrorMessage.jsx
**Responsibility**: Display errors gracefully

**Features**:
- Red theme for visibility
- Retry button (if applicable)
- Clear error messages

---

## State Management Strategy

### Why Context for Theme?
- Global state (needed everywhere)
- Doesn't change frequently
- Simple use case (no need for Redux)

### Why useState in App?
- Chat state is local to app
- Re-renders on every message (expected)
- Simple prop drilling (max 2 levels)

### When to Use Redux/Zustand?
If you add:
- User authentication
- Multiple chat sessions
- Complex form state
- Real-time sync

---

## API Integration

### Service Layer Pattern

**Why separate API service?**
- Centralized error handling
- Easy to mock for testing
- Switch backends easily
- Consistent error messages

### Error Handling Strategy

```js
try {
  // API call
} catch (error) {
  if (error.code === 'ECONNABORTED') {
    // Timeout
  } else if (error.response) {
    // Server error (4xx, 5xx)
  } else if (error.request) {
    // Network error
  } else {
    // Other errors
  }
}
```

### Retry Logic
- Store last user message
- On error, show retry button
- Retry sends same message again
- Remove failed message from history

---

## Styling Architecture

### Tailwind Approach

**Base Styles** (`@layer base`)
- CSS variables for theming
- Typography defaults
- Color scheme

**Components** (`@layer components`)
- Reusable patterns
- Button styles
- Form inputs

**Utilities** (`@layer utilities`)
- Custom scrollbar
- Animation helpers

### Dark Mode Implementation

```css
:root {
  --bg-primary: 255 255 255;
}

.dark {
  --bg-primary: 17 24 39;
}
```

**Why CSS variables?**
- Runtime theme switching (no recompile)
- Semantic naming
- Easy to customize

### Responsive Design

**Breakpoints**:
- Mobile first (default)
- `md:` - 768px+ (tablet)
- `lg:` - 1024px+ (desktop)

**Strategy**:
- Stack on mobile
- Side-by-side on desktop
- Touch-friendly targets (min 44px)

---

## Performance Optimizations

### Bundle Size
- Tree-shaking (Vite automatic)
- Dynamic imports (if needed)
- Minimal dependencies

### Rendering
- `React.memo` for MessageBubble (if performance issues)
- Virtualized list (for 1000+ messages)
- Debounced input (if needed)

### Network
- Request deduplication
- Caching (future: React Query)
- Optimistic updates (future)

---

## Accessibility (a11y)

### Implemented
- Semantic HTML (`<header>`, `<main>`, `<footer>`)
- ARIA labels on buttons
- Keyboard navigation
- Focus management
- Color contrast (WCAG AA)

### Screen Reader Support
- Messages announced as they arrive
- Input labeled properly
- Error messages descriptive

### Keyboard Shortcuts
- `Enter` - Send message
- `Shift+Enter` - New line
- `Tab` - Navigate elements

---

## Testing Strategy

### Unit Tests (Recommended)
```js
// Example with Vitest
import { render, fireEvent } from '@testing-library/react';
import InputBox from './InputBox';

test('sends message on Enter', () => {
  const onSend = vi.fn();
  const { getByRole } = render(<InputBox onSend={onSend} />);
  
  const input = getByRole('textbox');
  fireEvent.change(input, { target: { value: 'Hello' } });
  fireEvent.keyDown(input, { key: 'Enter' });
  
  expect(onSend).toHaveBeenCalledWith('Hello');
});
```

### Integration Tests
- Full chat flow (send message → receive response)
- Error handling
- Theme switching

### E2E Tests (Playwright/Cypress)
```js
test('can send and receive message', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await page.fill('textarea', 'I feel stressed');
  await page.click('button[type="submit"]');
  await expect(page.locator('.message-bot')).toBeVisible();
});
```

---

## Security Considerations

### Client-Side
- ✅ Input sanitization (trim, limit length)
- ✅ HTTPS only in production
- ✅ Environment variables for config
- ✅ No sensitive data in localStorage

### What Backend Should Handle
- Rate limiting
- Authentication/authorization
- Input validation
- SQL injection prevention
- XSS protection

---

## Future Architecture Improvements

### Scalability
1. **State Management**: Add Zustand/Redux for complex state
2. **Data Fetching**: Use React Query for caching
3. **Code Splitting**: Lazy load components
4. **PWA**: Add service worker for offline support

### Features
1. **WebSockets**: Real-time bidirectional communication
2. **Message Persistence**: LocalStorage or backend
3. **Multi-Session**: Handle multiple chat sessions
4. **Voice Input**: Web Speech API integration

### Performance
1. **Virtual Scrolling**: For 1000+ messages
2. **Image Optimization**: For message attachments
3. **CDN**: For static assets

---

## Development Workflow

### Local Development
```bash
npm run dev          # Start dev server
npm run build        # Production build
npm run preview      # Preview build locally
```

### Code Quality
```bash
npm run lint         # ESLint (add this)
npm run format       # Prettier (add this)
npm run type-check   # TypeScript (if migrating)
```

### Git Workflow
```bash
main              # Production
develop           # Integration
feature/chat-ui   # Feature branches
```

---

## Migration Paths

### To TypeScript
```bash
npm install -D typescript @types/react @types/react-dom
# Rename .jsx → .tsx
# Add types gradually
```

### To Next.js (for SSR)
```bash
npx create-next-app --example with-tailwindcss
# Move components
# Add API routes
```

### To React Native (mobile app)
```bash
npx react-native init ChatbotApp
# Reuse logic, rebuild UI
# Use React Native Paper
```

---

## Debugging Guide

### Common Issues

**Issue**: Messages not scrolling
**Debug**: Check `messagesEndRef` in ChatWindow

**Issue**: Theme not persisting
**Debug**: Check localStorage in DevTools

**Issue**: API calls failing
**Debug**: Network tab → Check request/response

### Developer Tools
- React DevTools (component tree)
- Redux DevTools (if using Redux)
- Network tab (API calls)
- Console (errors, logs)

---

## Performance Metrics

### Lighthouse Scores (Target)
- Performance: 95+
- Accessibility: 100
- Best Practices: 95+
- SEO: 90+

### Core Web Vitals
- LCP (Largest Contentful Paint): < 2.5s
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1

---

## Conclusion

This architecture provides:
- ✅ Clean separation of concerns
- ✅ Easy to understand and modify
- ✅ Scalable for future features
- ✅ Production-ready patterns
- ✅ Excellent developer experience

The component-based approach makes it easy to:
- Add new message types
- Implement new features
- Test in isolation
- Reuse in other projects

---

## Resources

- [React Docs](https://react.dev)
- [Vite Guide](https://vitejs.dev/guide/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Axios Docs](https://axios-http.com/docs/intro)

---

**Questions?** Review the README.md or check component comments.