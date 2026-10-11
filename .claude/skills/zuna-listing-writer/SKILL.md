---
name: zuna-listing-writer
description: >-
  Write holiday home listings for Airbnb, Booking.com and Vrbo for ZUNA Vacation
  Homes: a title of 50 characters or less, description, house rules and an
  amenities checklist. Never guesses amenities, asks for missing facts as [ ]
  items, reminds about the DET permit number and the guest ID/registration rule,
  and never sets the price. Use when the user says "listing likho", "Airbnb
  listing", "Booking.com description", "Vrbo listing", "listing title", or
  wants to update a listing's text.
---

# zuna-listing-writer

Airbnb, Booking.com aur Vrbo ke liye listing text likhta hai. Yeh skill **sirf text** deta hai.
Listing publish ya update karna CLAUDE.md ke hisaab se Zeeshan ki haan ke baad hi hoga.

## Pehle yeh padho

- Repo root ka `CLAUDE.md` (business, approval rules, Never list).
- Zeeshan ne jo details di hain: building, area, unit type (studio/1BR...), stay type (daily/monthly),
  photos ka description, aur confirmed amenities.

## Step 1: Facts collect karo, gadho mat

Jo cheez Zeeshan ne confirm nahi ki, use listing me **mat likho**. Uski jagah ek `[ ]` sawaal banao.
Pehle yeh checklist dikhao aur jawab maango:

```
LISTING FACTS - confirm karein (✓ = haan, ✗ = nahi)
[ ] Building aur area ka naam (unit number NAHI)
[ ] Unit type aur size (sq ft)
[ ] Kitne guests max
[ ] Beds: kitne aur kaunse (king/queen/sofa bed)
[ ] Bathroom(s)
[ ] Check-in / check-out time
[ ] Stay type: daily, monthly, ya dono
[ ] Minimum nights
[ ] DET holiday home permit number
[ ] Cancellation policy (platform ki kaunsi policy)
```

```
AMENITIES - sirf confirmed wale listing me jayenge
[ ] Wi-Fi                      [ ] Air conditioning
[ ] Kitchen / kitchenette      [ ] Washing machine
[ ] Fridge, microwave, stove   [ ] Iron / hair dryer
[ ] TV / streaming             [ ] Work desk
[ ] Pool                       [ ] Gym
[ ] Parking                    [ ] Balcony
[ ] View (kaunsa)              [ ] 24h security / reception
[ ] Towels & linen             [ ] Basic toiletries
[ ] Cleaning (kitni baar)      [ ] Metro / landmark se doori
```

Jo `[ ]` khaali reh jaye, wo final output me **"Missing"** list me jayega.

## Step 2: Listing likho

### Title
- **Max 50 characters**, teeno platforms ke liye. Characters gin kar `(xx/50)` likho.
- Building/area + unit type + ek asli fayda. Jaise: `Furnished Studio, Business Bay, Monthly Stays (45/50)`.
- "Luxury", "Amazing", "Best" jaise khokhle shabd, aur emoji/ALL CAPS nahi.

### Description
- Pehli 2 lines me: kahan hai, kya hai, kiske liye perfect hai.
- Phir chhote paragraphs: the space, location (sirf asli landmarks), guest access, stay info.
- Sirf confirmed amenities. Andaaze se "pool", "view", "gym" kabhi nahi.
- Monthly stay likh sakte ho. **Sale ya yearly rent ka zikr nahi** (RERA licence nahi hai).
- Unit number, owner ka naam/phone, ya koi personal data nahi.
- End me: `Hosted by ZUNA Vacation Homes. Where comfort begins.`

### House rules
Sirf Zeeshan ke confirm kiye rules. Default sawaal `[ ]` me poochho:

```
[ ] Smoking allowed? (inside / balcony / nahi)
[ ] Parties / events?
[ ] Pets?
[ ] Visitors ki limit / time?
[ ] Quiet hours?
[ ] Building ke apne rules (pool timing, gym access card)?
```

Ek rule hamesha rakho (yeh compliance hai, guess nahi):
`All guests must share a valid passport or Emirates ID before check-in for registration, as required for Dubai holiday homes.`

### Platform notes
- **Airbnb:** title 50 char, "The space", "Guest access", "Other things to note" sections.
- **Booking.com:** property description, house rules aur facilities alag fields me jaate hain. Facilities
  sirf ticked checklist se.
- **Vrbo:** headline + description. Monthly stays ko clearly likho.

## Step 3: Reminders (har output ke end me)

```
REMINDERS
- DET permit number: listing me dikhana zaroori hai. {number ya "MISSING - add karein"}
- Guest ID: har guest ka passport/Emirates ID check-in se pehle lena aur DET system me register karna.
  ID ki copy repo, chat ya listing me kabhi save nahi karni.
- Price: yeh skill price set nahi karta. Rate Zeeshan khud platform par daalenge: {{price}}
- Publish: nayi listing ya bada badlaav sirf Zeeshan ki haan ke baad.
```

Exact niyam (jaise registration ki deadline) badal sakte hain, isliye DET ki official guidance se confirm
karne ko kaho. Apni taraf se koi deadline ya fine mat likho.

## Output format

CLAUDE.md ke hisaab se **do output**:

1. **Draft:** facts se seedha bana hua version.
2. **Behtar version:** wahi facts, behtar pehli line, saaf structure, koi naya claim nahi.

Phir:

```
LISTING READY (draft only)
title:      {xx}/50 chars
amenities:  {n} confirmed, {m} missing
missing:    {list of [ ] items}
permit:     {DET permit status}
price:      not set (Zeeshan)
```

Aakhri line: **"Kya change karein, ya missing details bhej dein?"** Kuch bhi publish nahi karna.
