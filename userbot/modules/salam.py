from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ππππππππππππππ πππππ ππππ...")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ππππππππππππππ.... ππππππππππ!!!!")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("πππππππππππππ πππππ ππππ...")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ππππππππππππππ ππππ ππππππ......")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππ ππππ ππππ ππ πππ π ππππππ πππππ**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πππ πππππ ππ π πππππ ππππ ππππππ, ππ πππ πππππ ππππππππ ππΈπ¬π’πΈπ¬**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πππππ ππππ ππ πππππππππ!!!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππ ππ πππ π πππππ ππππ π€**")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**π πππππ ππππ ππππππ, πππππ ππππ ππ ππ ππππππ πππ π πππππ ππππππ**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππ ππ ππππ, ππππππ πππ πππππ π π πππππππ!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππππ πππππ πππ ππππππ!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππ ππππ πππ π ππππππ πππππ, ππππππ ππππππ ππ πππππππππ ππππ ππππππ, ππ πππππ ππππππ βοΈ!!**")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πππππ ππππππ ππ, πππππ πππππππ!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππππ ππππ  ππππ ππππππ ππππ ππππ ππππππ πππππ­**")


@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππ ππ πππππ ππ πππ? πππππππ ππππ ππ ππππππ ππππ ππ πππππ**")


@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππππ πππ πππ πππ ππ ππππππ ππ πππ ππππππππ πππππ ππππππ­**")


@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**πππππ ππππ ππππ ππππππ ππππ ππ πππ π ππππ ππππ 5 ππππ ππ**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππππππ ππ πππππ ππππ πππππ ππππ π πππππ πππ ππππππ ππ π πππππ πππππ**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ππ’π¬ π¬π¦π³π¦π― π­πΆ π£π¦π¨πͺπ΅πΆ π΅π°π­π°π­, π¬πΆπ£πΆπ³π’π― π£π’π±π’π¬ π­πΆ π¨πΈ π¨π’π­πͺ π£πΆπ’π΅ π₯πͺπ«π’π₯πͺπͺπ― π¬π°π­π’π? π³π¦π―π’π―π¨ π’π―π’π¬ π±π’πΆπ₯.ππΆπͺπ©π©π©π©π©!!!**")

CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Untuk mengontoli mereka.\
\n\nN\
\nUsage: Kalo kesel coba aja.\
\n\nB\
\nUsage: Buat Ngatain Yang Suka Bacot.\
\n\nM\
\nUsage: Tersedak meledek.\
\n\nY\
\nUsage: Buat yang males adu bacot.\
\n\nC\
\nUsage: Buat menghujat.\
\n\nS\
\nUsage: Haha sokap."
})

CMD_HELP.update({
    "salam2":
    "V\
\nUsage: Hujat Orang caper.\
\n\nJ\
\nUsage: Hujat Jamet.\
\n\nA\
\nUsage: Hujat yang gapunya muka.\
\n\nX\
\nUsage: Ngatain Grup wkwk.\
\n\nZ\
\nUsage: teruntuk petarung.\
\n\nH\
\nUsage: Coba dewek ah.\
\n\n.atg\
\nUsage: Istighfar 1.\
\n\n.ast\
\nUsage: Istighfar 2.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri."
})
