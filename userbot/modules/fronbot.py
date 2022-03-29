from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah aku bukan type mu 😊`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.lu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lu Peler☑️**")
    await typew.edit("**Lu Peler✅**")
    sleep(2)
    await typew.edit("**Lu Gilaa☑️**")
    await typew.edit("**Lu Gilaa✅**")
    sleep(2)
    await typew.edit("**Lu Depresi☑️**")
    await typew.edit("**Lu Depresi✅**")
    sleep(2)
    await typew.edit("**Lu Gajelas☑️**")
    await typew.edit("**Lu Gajelas✅**")
    sleep(2)
    await typew.edit("**Lu goblok!☑️**")
    await typew.edit("**Lu Goblok banget!✅**")
    sleep(2)
    await typew.edit("**Lu kang gabut!☑️**")
    await typew.edit("**Lu kang gabut!✅**")
    sleep(2)
    await typew.edit("**Lu,MengRibet☑️**")
    await typew.edit("**Lu,MengRibet✅**")
    sleep(2)
    await typew.edit("**Penggali,Mengintil☑️**")
    await typew.edit("**Penggali,Mengintil✅**")
    sleep(2)
    await typew.edit("**CUMA FRON YANG BENER !**")
    sleep(3
)

@register(outgoing=True, pattern='^.lah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")
    
@register(outgoing=True, pattern='^.gc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`SUPPORT.. `")
    sleep(1)
    await typew.edit("`CENGHA...`")
    sleep(1)
    await typew.edit("`SUCCESSFULLY COMPELED`")
    sleep(1)
    await typew.edit("`💀SUPPORT` @jakanasokin 💀 CENGHA` @fronsjahh")




CMD_HELP.update({
    "fron":
    "`.fron`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \n\n`.lah`\
    \nUsage: hiks\
    \n\n`.gc`\
    \nUsage: support\
    \n\n`.punten` ; `.fron`\
    \nUsage: misi."
})
