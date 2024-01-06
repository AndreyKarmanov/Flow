import type { Metadata } from 'next'
import { Inter, Kadwa } from "next/font/google";
import './globals.css'

const inter = Inter({ subsets: ['latin'] })
const kadwa = Kadwa({
  subsets: ["devanagari"],
  weight: ["400", "700"],
});

export const metadata: Metadata = {
  title: 'Flow',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${kadwa.className} ${inter.className}`}>{children}</body>
    </html>
  );
}
