
from discord.ext import commands
import asyncio

class art:
    """lul"""
    def __init__(self, bot):
    	self.bot = bot

    @commands.command(pass_context=True)
    async def art(self, ctx, times : int=None):
        """\U00000028 \U00000361\U000000b0 \U0000035c\U00000296 \U00000361\U000000b0\U00000029"""
        if times == None:
            times = 1
        elif times > 50:
            times = 50
        delay = ((times * 1.00 / 10) + 0.3)
        counter = 0
        while counter < times:
            await self.bot.edit_message(ctx.message, ':kissing_closed_eyes:  :flushed: ')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':kissinf_heart:  :heart_eyes:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':smiling_imp::knife:  :scream:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':imp: :knife:    :raised_back_of_hand::slight_smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':fearful:  :gun::slight_smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':runner::dash:  :sweat_smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':kissing_smiling_eyes:  :grin:')
            await asyncio.sleep(delay)
            counter = counter + 1

def setup(bot):
	bot.add_cog(Art(bot))







