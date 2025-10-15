import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Arrow Tuning System',
  description: 'Privacy-first performance monitoring platform',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

