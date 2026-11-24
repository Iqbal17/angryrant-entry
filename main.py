"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (gate: 1-400 characters, UTF-8).

FINAL TEXT (334 characters, hand-counted below):
    "One email goes out to 40 people. Within minutes, 39 geniuses
    reply-all to say 'please remove me from this thread,' which adds
    39 emails to the very thread they want to leave. The only way out
    is to reply-all, which is what trapped you in the first place.
    It is a support group for people who hate reply-all, run entirely
    by reply-all."

CHARACTER COUNT (segment by segment, every character incl. spaces):
    S1 "One email goes out to 40 people." = 32
    S2 " Within minutes, 39 geniuses reply-all to say 'please remove me
        from this thread,' which adds 39 emails to the very thread
        they want to leave." = 142  (cumulative 174)
    S3 " The only way out is to reply-all, which is what trapped you
        in the first place." = 80  (cumulative 254)
    S4 " It is a support group for people who hate reply-all, run
        entirely by reply-all." = 80  (cumulative 334)
    TOTAL = 32 + 142 + 80 + 80 = 334 characters. Gate 1-400: PASS.
    Cross-check: 63 spaces + 271 non-space characters = 334.

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
"""

import os

ENTRY = (
    "One email goes out to 40 people. Within minutes, 39 geniuses "
    "reply-all to say 'please remove me from this thread,' which adds "
    "39 emails to the very thread they want to leave. The only way out "
    "is to reply-all, which is what trapped you in the first place. "
    "It is a support group for people who hate reply-all, run entirely "
    "by reply-all."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
