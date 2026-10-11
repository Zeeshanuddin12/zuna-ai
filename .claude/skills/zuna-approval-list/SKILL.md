---
name: zuna-approval-list
description: >-
  Build Zeeshan's daily morning approval list for ZUNA Vacation Homes: up to 10
  items that fit in a 1-hour review, grouped as "Aaj approve karo", "Jawab ka
  intezaar" and "Risk/alert", in simple Hinglish, following CLAUDE.md's approval
  rules. Use when the user says "aaj ki approval list", "morning list", "kya
  approve karna hai", "daily approvals", or at the start of a working day.
---

# zuna-approval-list

Roz subah Zeeshan ke liye ek list banata hai, jise wo **1 ghante ke andar** padh kar haan/na bol sake.
Yeh skill sirf list banata hai. Kuch bhejta, post ya publish nahi karta.

## Pehle yeh padho

1. Repo root ka `CLAUDE.md`. Approval rules, message style aur "Never" list wahi se aate hain.
2. Is session me jo drafts, guest messages, owner chats, listing changes ya posts pending hain,
   wahi is list ka material hai. Agar kuch nahi diya gaya, to Zeeshan se ek baar poochho:
   "Aaj kya pending hai? Messages, drafts ya bookings paste kar dijiye."
   Kabhi bhi item gadho mat.

## Kya list me aata hai (aur kya nahi)

CLAUDE.md ke hisaab se **sirf yeh cheezein Zeeshan ki haan maangti hain**, isliye "Aaj approve karo"
me sirf yahi aayengi:

- Price change
- Refund / cancellation
- Nayi listing publish karna
- Owners / leads ko koi bhi WhatsApp
- Koi bhi social post

Jo kaam AI khud kar sakta hai (guest ke aam sawaal, approved check-in instructions, listing photos,
review maangna, calendar/availability), unhe list me **mat daalo**. Unka sirf ek line ka count
"Risk/alert" ke neeche de sakte ho, jaise "Aaj AI ne khud 6 guest sawaalon ke jawab diye."

## Sections

```
☀️ AAJ KI APPROVAL LIST - {date}        (kul samay: ~{N} min / 60 min)

1) AAJ APPROVE KARO
   [1] {kya}  ·  {kiske liye}  ·  ~{min} min
       Kyun: {ek line}
       Draft:   {tool ka draft}
       Behtar:  {behtar version}
       Faisla:  Haan / Na / Badlo

2) JAWAB KA INTEZAAR
   [n] {kis ka jawab}  ·  {kab se}  ·  agla step: {ek line}

3) RISK / ALERT
   [n] {kya khatra}  ·  {kya karna chahiye}
```

## Rules

- **Max 10 items** teeno sections ko mila kar. Zyada hon to sabse zaroori 10 rakho aur neeche likho
  "Baaki {x} kal ki list me."
- **Kul samay 60 min se kam.** Har item ke saath andaza (min) likho. Total upar dikhao.
- **Order:** jo paisa ya guest ka stay turant badalta hai (refund, aaj ka check-in, price) wo sabse upar.
- **Do output:** har "Aaj approve karo" item me tool ka draft **aur** behtar version, dono. Faisla Zeeshan ka.
- **Message style** (CLAUDE.md): owners/leads ke messages chhote, casual, human. `Mr <name>` likho,
  "sir" nahi. Message "thanks" se shuru nahi. Guests/leads ko pehli line me batao ki yeh ZUNA ka
  AI assistant hai.
- **Price kabhi khud set mat karo.** Price wale item me `{{rate - Zeeshan batayenge}}` chhodo.
- **Personal data list me nahi:** phone, unit number, passport, ID. Guest/owner ko naam ke pehle
  akshar ya booking reference se pehchaano.
- **Risk/alert me hamesha check karo:**
  - Koi draft sale ya yearly rent ka ad to nahi ban raha (RERA licence nahi hai).
  - Kisi post me unit number ya owner ka phone to nahi.
  - Bulk / unsolicited message, scraping ya LinkedIn automation ka koi plan to nahi.
  - Listing me DET permit number missing to nahi.
  - Aaj ya kal ke check-in ke liye guest ID / registration pending to nahi.
- Hinglish simple rakho. Technical shabd mat use karo.

## Kya nahi karna

- Kuch bhi send, post, publish ya schedule nahi karna. Zeeshan "haan" bole tab bhi, us item ka
  agla step alag se poochh kar hi karna.
- List ko repo me save nahi karna, kyunki usme guest/owner ki details ho sakti hain. Sirf chat me dikhao.

## End me

List ke baad ek line: **"Kaunsa number approve karein? Jaise: 1 haan, 2 badlo, 3 na."**
