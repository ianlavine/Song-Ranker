import NextAuth from 'next-auth'
import Providers from 'next-auth/providers'
import { PrismaAdapter } from '@next-auth/prisma-adapter'
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

export default NextAuth({
  providers: [
    Providers.Credentials({
      name: 'Credentials',
      credentials: {
        username: { label: "Username", type: "text", placeholder: "jsmith" },
        password: {  label: "Password", type: "password" }
      },
      async authorize(credentials) {
        // Add your own logic here to find the user in the database
        const user = await prisma.user.findUnique({ where: { email: credentials.username } })
        if (user && user.password === credentials.password) {
          return user
        } else {
          return null
        }
      }
    })
  ],
  adapter: PrismaAdapter(prisma),
})
