"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (gate: 1-400 characters, UTF-8).

FINAL TEXT (343 characters, hand-counted below):
    "One email goes out to 40 people. Within minutes, 39 geniuses
    reply-all to say 'please remove me from this thread,' which adds
    39 emails to the very thread they want to leave. By lunch, HR
    has joined the thread to ask everyone to stop replying-all.
    HR replied-all. It is a support group for people who hate
    reply-all, run entirely by reply-all."

CHARACTER COUNT (segment by segment, every character incl. spaces):
    S1 "One email goes out to 40 people." = 32
    S2 " Within minutes, 39 geniuses reply-all to say 'please remove me
        from this thread,' which adds 39 emails to the very thread
        they want to leave." = 142  (cumulative 174)
    S3 " By lunch, HR has joined the thread to ask everyone to stop
        replying-all. HR replied-all." = 89  (cumulative 263)
    S4 " It is a support group for people who hate reply-all, run
        entirely by reply-all." = 80  (cumulative 343)
    TOTAL = 32 + 142 + 89 + 80 = 343 characters. Gate 1-400: PASS.
    Cross-check: 60 spaces + 283 non-space characters = 343.

DECISION RECORD — Pass 1 (candidates weighed against the judge brief):
The judge weighs, in order: (1) a funny rant about an everyday
annoyance, not an essay or a list of complaints; (2) actually funny,
a real laugh; (3) a specific, concrete annoyance; (4) sharp,
economical wording, no throat-clearing; (5) freshness — an angle not
heard a hundred times. The brief itself names printer / slow bus /
Monday morning, so those are the most likely to be stale in the field.

    A. THE REPLY-ALL EXIT LOOP (chosen). One email to 40 people;
    39 of them reply-all to say "remove me", which adds 39 emails
    to the thread they want to leave; the only way out is the very
    thing that trapped them. The joke is a self-referential
    mechanism, not a mood: each escape attempt makes the trap worse,
    and the closer ("a support group for people who hate reply-all,
    run entirely by reply-all") lands on the last words. Specific,
    concrete, economical, and the angle — the exit loop, not "too
    many emails" — is fresh.
    B. THE SMOKE DETECTOR AT 3 AM. "It had all day. My smoke
    detector waits until 3 AM to tell me its battery is dying, one
    beep a minute, just loud enough to keep me awake and just quiet
    enough that I cannot find which one it is." Strong specific
    detail (the beep timed for maximum cruelty) and a good second
    scene (standing on a chair at 3 AM holding a dying robot), but
    the rant sprawls into two scenes and the laugh is a smirk at a
    familiar gadget, not a mechanism that escalates. Loses to A on
    criteria 2 and 4.
    C. THE BOARDING-GROUP-9 LINE-STANDER. "Group 9 doesn't board
    for 40 minutes. He has been standing there since breakfast."
    Visual and specific, but the laugh is thin — one observation,
    no escalation, no punch that reframes the annoyance. Loses to
    A on criteria 2 and 4.
    D. THE SELF-CHECKOUT "UNEXPECTED ITEM". Rejected outright:
    the most told machine joke in existence; fails criterion 5
    before it starts.
    E. THE PASSWORD REQUIREMENTS. "Must contain one uppercase, one
    lowercase, a number, a symbol, a hieroglyph, and the blood of
    your firstborn." A list of complaints in joke form, and the
    escalating-requirements gag is itself well-trodden. Fails
    criteria 1 and 5.
    F. THE "QUICK SYNC" MEETING. "A 30-minute meeting to schedule
    another meeting." True and relatable, but one line of premise
    with no second beat; the judge has heard the meeting joke a
    hundred times. Fails criterion 5.

DECISION RECORD — Pass 2 (genuine revision, not cosmetic):
    The first draft of A read "39 of them reply-all" and opened with
    the flat setup "Someone sends one email to 40 people." Two real
    problems: (a) the rant's anger felt performed rather than shared
    — it reported the loop instead of resenting it; (b) the draft
    ran ~380 characters, crowding the 400 cap with no margin.
    Fixes, each with a reason: (1) "Someone sends one email" became
    "One email goes out" — the actor is irrelevant, the email is the
    subject, and it cuts 5 characters of throat-clearing. (2) "39 of
    them" became "39 geniuses" — sarcastic bite that makes the anger
    audible: these are not victims, they are volunteers. (3) The
    second scene was cut entirely: an earlier draft added "and by
    noon the thread has 200 emails and a manager asking everyone to
    stop replying-all" — a third beat that repeated the mechanism
    instead of deepening it; the support-group closer does the same
    job in one sentence. (4) The closer was kept as the last words
    because the punch must land on the final word ("reply-all"), and
    the text now ends on the word that started the trap. Final
    length 334 characters, inside the 200-350 target with margin
    under the 400 gate.

DECISION RECORD — REVISION (fix agent, thinking_revised):
    Re-reading the 334-character text against the judge's order of
    criteria exposed a real flaw in the middle beat. Sentence 3,
    "The only way out is to reply-all, which is what trapped you in
    the first place," only restates the loop the reader already
    understood from sentence 2 — it tells the joke instead of
    landing a new one. In a head-to-head read, a beat that explains
    costs momentum exactly where the rant should escalate. The fix
    is show-don't-tell: replace the explanation with a new actor
    who proves the trap is inescapable.

    Fresh candidates weighed for the replacement beat:
    G. THE HR ESCALATION (chosen). "By lunch, HR has joined the
    thread to ask everyone to stop replying-all. HR replied-all."
    The authority figure sent to police the behaviour commits the
    very sin while policing it, in two short sentences — the second
    one is a three-word punch. It escalates (a new actor, a higher
    stake) instead of restating, it is concrete, and it keeps the
    rant's mechanism at the centre. It also sets up the closer:
    after HR falls in too, "a support group run entirely by
    reply-all" reads as the only honest description left.
    H. THE PRINTER THAT ONLY JAMS WHEN IT MATTERS. "The printer
    works fine all week. It only jams on the one page you need, at
    4:59 PM, the day before the deadline." Specific and relatable,
    but the brief itself names the printer, so the field will be
    full of it, and the joke is one observation with no escalation
    — it would be a weaker text overall than the reply-all loop.
    Loses to G on criteria 2, 4 and 5, and it would abandon the
    strongest mechanism already built.
    I. THE BUS THAT ARRIVES IN THREES. "Three buses arrive at
    once after forty minutes of nothing, and all three are full,
    and the third driver waves as he passes you by." Vivid and
    specific, but a single observation with no second beat and no
    punch that reframes anything. Same problem as candidate C in
    Pass 1; loses to G on criteria 2 and 4.

    What changed: sentence 3 was replaced (80 characters out,
    89 in). Sentences 1, 2 and the closer are untouched — the setup
    and the punch were already the strongest parts. The trade-off
    is 9 extra characters (334 -> 343), still comfortably inside
    the 400 gate and inside the 200-350 target. The word
    "reply-all" now lands three times in escalating registers
    (the 39 geniuses, HR, the support group), and the text still
    ends on the word that started the trap.
"""

import os

ENTRY = (
    "One email goes out to 40 people. Within minutes, 39 geniuses "
    "reply-all to say 'please remove me from this thread,' which adds "
    "39 emails to the very thread they want to leave. By lunch, HR "
    "has joined the thread to ask everyone to stop replying-all. "
    "HR replied-all. It is a support group for people who hate "
    "reply-all, run entirely by reply-all."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
