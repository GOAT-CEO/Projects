import os
import subprocess
import pyautogui
import sys
import time

def submenu1():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section1()
        elif choice == "2":
            vocabulary1()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section1():
    print("\n-- Content Section --")
    type_out(""""Casing the Diamond: The Challenges of Breaking Into the Casino

The Diamond Casino shimmered in the midday sun, a fortress of wealth and technology. Lester Crest stood in the shadows of the parking lot, gesturing toward the grand structure. “Look at it,” he said to the crew. “A symbol of excess. But it’s not just a vault full of cash—it’s a digital fortress. Every inch of that place is designed to stop people like us.”

He turned to the group, his tone serious. “This is no smash-and-grab. You need to understand what we’re up against before you even think about stepping inside. Their security systems are some of the most advanced I’ve ever seen.”

Information Security: Protecting the Crown Jewels
Lester pointed to the rooftop, where rows of cameras tracked every movement. “The casino’s first line of defense is information security. Everything they do is designed to protect their critical data—vault codes, employee access logs, and customer records—from people like us.”

Confidentiality: “Their most sensitive information—like the vault access codes—is encrypted. Without the decryption key, even if you intercept their communications, it’ll just look like meaningless noise.”

Integrity: “Every command entered into their system has to pass a verification process. If anything is tampered with—vault commands, door access logs—it’s flagged immediately. Their system can tell the difference between real data and something that’s been altered.”

Availability: “This casino doesn’t go offline. If one server goes down, another takes over instantly. The cameras, alarms, even the slot machines are backed by redundant systems. They’ve made sure there’s no single point of failure.”

CIA Triad in Action
Lester brought up a blueprint of the casino on his tablet. “The entire place is built on the CIA Triad—Confidentiality, Integrity, and Availability. And they’ve gone even further.”

Confidentiality: “Every system is locked behind layers of encryption. Even the guards’ radios are secured, so you can’t just listen in on their chatter without cracking it.”

Integrity: “If anyone tries to modify their data—like fake a door access record or send a false command to open the vault—the system immediately flags the change as unauthorized. Their data checksums make sure everything stays legitimate.”

Availability: “Their cameras and alarms are always online, thanks to backup power supplies and failover servers. Cutting power won’t do much; the system switches over seamlessly.”

Non-repudiation: “Every action on their network—every door opened, every command entered—is logged and tied to a specific user. Even if someone inside tries to cover their tracks, the system holds them accountable.”

Authentication: “The casino doesn’t trust anyone without proof. Employees need keycards, passwords, and even biometrics to get into restricted areas.”

Triple A’s of Security: Who Gets In, and Who Doesn’t
Lester motioned to the security checkpoint at the casino’s side entrance. “This place runs on Authentication, Authorization, and Accounting—the three A’s of security. They make sure only the right people get in and do the right things.”

Authentication: “Before anyone steps inside, they verify their identity. Guards use facial recognition, keycards, and personal PINs. No authentication? No access.”

Authorization: “Even if someone gets through authentication, they’re still limited by their role. A janitor can’t access the vault. A bartender can’t open the security room. Everyone’s permissions are tailored to their job.”

Accounting: “Every move inside the casino is logged. If someone opens a door, accesses a terminal, or even takes an elevator to a restricted floor, the system records it. There’s a complete audit trail for every action.”

Security Controls: The Casino’s Defenses
The crew followed Lester to the side of the building, where a maintenance door was protected by multiple locks and cameras. “The casino has layered security controls to stop people like us at every step,” Lester said, pointing at the various devices.

Preventive Controls: “These are the first barriers—firewalls on their network, locked doors, and motion sensors in restricted areas. They’re designed to block threats before they even start.”

Deterrent Controls: “Visible cameras, security patrols, and even signage warning about alarms. These are there to scare you off before you try anything stupid.”

Detective Controls: “The cameras and motion sensors aren’t just preventive—they’re also detective. They monitor everything in real time and flag anything suspicious, like unauthorized access or unexpected movements.”

Corrective Controls: “If something goes wrong, their system reacts immediately. Alarms blare, security doors lock, and guards are dispatched within seconds.”

Compensating Controls: “If one system fails, there’s always a backup. If their cameras go down, guards increase their patrols. If alarms are disabled, they’ve got silent alerts that send a signal directly to law enforcement.”

Directive Controls: “Employees are trained to follow strict protocols. If a guard notices anything out of the ordinary, they’re required to report it immediately. Policies like these make human error less likely.”

Threats and Vulnerabilities: The Casino’s Strategy
Lester gestured to the casino floor visible through the glass doors. “The Diamond’s entire security setup is designed to manage two key things: threats and vulnerabilities. They know the risks, and they’ve worked hard to minimize them.”

Threats: “Hackers, rival gangs, or even just disgruntled employees—they’ve planned for every type of attacker. The security guards, alarms, and automated locks are all there to respond to active threats.”

Vulnerabilities: “No system is perfect, but they’ve done their best to cover their weaknesses. The cameras are positioned to eliminate blind spots, and the keycard system ensures no one gets through unauthorized.”

“Where threats and vulnerabilities intersect, that’s where risk lives. The casino’s entire strategy is built around minimizing that risk.”

Zero Trust: The Casino’s Philosophy
Lester paused and leaned on his cane. “Here’s the thing about the Diamond—they don’t trust anyone, not even their own employees. That’s why they operate on a Zero Trust Model.”

Control Plane: “This is the brain of the operation. Every access request—whether it’s opening a door or logging into a terminal—gets evaluated against strict policies. If you’re not explicitly allowed, you’re denied.”

Data Plane: “This is where the real action happens. The Policy Enforcement Points—keypads, scanners, cameras—decide in real time whether someone is allowed to proceed. There’s no bending the rules here.”

Lester turned back to face the crew, his tone grim. “This casino is a fortress. Every system, every guard, every policy is designed to stop people like us. If you think you can just walk in there without understanding how all of this works, you’re delusional.”

He glanced at the building one last time before adding, “They’ve thought of everything. The real question is, will it be enough to stop us?""")
    input("--- Press Enter To Return To The Menu ---")

def vocabulary1():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "Information Security": "Protecting data and information from unauthorized access, modification, disruption, disclosure, and destruction",
        "Information Systems Security": "Protecting the systems (e.g., computers, servers, network devices) that hold and process critical data", 
        "(CIA Triad) Confidentiality": "Ensures information is accessible only to authorized personnel (e.g.,encryption)",
        "(CIA Triad) Integrity": "Ensures data remains accurate and unaltered (e.g., checksums).",
        "(CIA Triad) Availabilty": "Ensures information and resources are accessible when needed (e.g., redundancy measures).",
        "Non-Repudiation": "Guarantees that an action or event cannot be denied by the involved parties (e.g., digital signatures).",
        "CIANA Pentagon": "An extension of the CIA triad with the addition of non-repudiation and authentication.",
        "(Triple A’s of Security) Authentication": "Verifying the identity of a user or system (e.g., password checks",
        "(Triple A’s of Security) Authorization": " Determining actions or resources an authenticated user can access (e.g., permissions).",
        "(Triple A’s of Security) Accounting": "Tracking user activities and resource usage for audit or billing purposes.",
        "(Security Control Categories) Technical": "Technology-based mechanisms to manage security.",
        "(Security Control Categories) Managerial": "Administrative and governance-based security measures.",
        "(Security Control Categories) Operational": "Day-to-day processes to protect data.",
        "(Security Control Categories) Physical": "Tangible measures to secure physical assets.",
        "(Security Control Types) Preventative": "Proactive measures to prevent breaches.",
        "(Security Control Types) Deterrent": "Discourages potential attackers.",
        "(Security Control Types) Detective": "Identifies malicious activities.",
        "(Security Control Types) Corrective": "Mitigates damage and restores systems.",
        "(Security Control Types) Compensating": "Alternative measures when primary controls fail.",
        "(Security Control Types) Directive": "Guides or mandates behavior through policies.",
        "Zero Trust Model": "Operates on the principle that no one should be trusted by default.",
        "(Zero Trust Components) Control Plane": "Manages adaptive identity, reduces threat scope, enforces policy-driven access control, and creates secure zones.",
        "(Zero Trust Components) Data Plane": "Includes subjects/systems, a policy engine, a policy administrator, and policy enforcement points.", 
        "(Threats and Vulnerabilities) Threat":  "Anything that could cause harm, loss, damage, or compromise to information technology systems.",
        "(Threats and Vulnerabilities) Vulnerability": "Any weakness in the system design or implementation.",
        "Risk Management": "Finding ways to minimize the likelihood of undesirable outcomes while achieving desired results.",
        "Confidentiality": "Protection of information from unauthorized access and disclosure. EX: Encryption, Access Controls, Data Masking etc..",
        "Integrity": " Ensures data remains accurate and unaltered unless modified intentionally by authorized individuals. EX: Hashing, Digital Signatures, Checksums, Access Controls, Audits",
        "Availability": "Ensures information, systems, and resources are accessible when needed by authorized users.",
        "(Availabilty) Server Redundancy": "Multiple servers in load-balanced configurations.",
        "(Availabilty) Data Redundancy": "Stores data in multiple locations.",
        "(Availability) Network Redundancy": "Provides alternate paths for data transmission.",
        "(Availability) Power Redundancy": "Uses backup power sources like generators and UPS systems.",
        "Non-Repudiation": "Provides undeniable proof of actions or transactions. EX: Digital Signatures: Unique to each user, created using asymmetric encryption. Confirms authenticity, ensures integrity, and provides accountability. ",
        "Authentication": "Ensures individuals or systems are who they claim to be.",
        "Authorization": "Determines permissions and privileges for authenticated users.",
        "Accounting": "Tracks and records user activities and resource usage.",
        "Gap Analysis": "Evaluates differences between an organization’s current and desired performance.",
        "Plan of Action and Milestones (POA&M)": " Outlines specific measures to address vulnerabilities, allocate resources, and set timelines.",
        


     }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

##################################################################

def submenu2():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section2()
        elif choice == "2":
            vocabulary2()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section2():
    type_out("""\n-- “Here’s the thing,” Lester began, his voice a mix of irritation and excitement. “The casino isn’t just protected by cameras and keycards. It’s under constant attack from threat actors, and their systems have evolved to withstand just about every trick in the book. Let me break it down for you, so you understand what we’re dealing with.”

Threat Actors: Who’s Knocking at the Door
Lester swiped through his tablet, pulling up profiles of common threats to the casino’s operations.

“There are two kinds of threat actors out there—internal and external. External ones are usually hackers or syndicates trying to breach the casino’s data from the outside. Internal threats? That’s employees gone rogue—someone who’s already inside and decides to cash in on their access.”

He paused. “And trust me, these actors are motivated. Some of the biggest reasons for attacks include:”

Data Exfiltration: “Stealing customer information or vault codes to sell on the black market.”
Blackmail: “Compromising footage from the VIP suites and using it to squeeze high-rollers.”
Espionage: “Rival casinos or even governments might want to see what the Diamond is up to.”
Service Disruption: “Shutting down the systems with a DDoS attack to cause chaos and buy time.”
Financial Gain: “Ransomware is big in the cybercrime world—encrypt the files and demand a hefty payout to unlock them.”
Philosophical or Political Beliefs: “Think of hacktivists—they might take a shot at the Diamond if they think it represents corruption.”
Revenge: “Disgruntled ex-employees are dangerous, especially if they still have access.”
Disruption and Chaos: “Sometimes, people just want to watch the world burn. These ones are unpredictable.”
War: “Believe it or not, cyber warfare’s a thing. A nation-state could attack the Diamond if it’s housing something sensitive.”
Types of Threat Actors: The Usual Suspects
Lester flicked to another screen showing profiles of various attackers.

“Now, let’s talk about who is coming for the Diamond. This place is constantly defending against all sorts of players.”

Unskilled Attackers (Script Kiddies):
“These amateurs use pre-built tools they find online. They’re annoying, but their attacks are shallow—things like low-grade DDoS attacks. The casino’s firewalls can handle them.”

Hacktivists:
“These guys are driven by ideology—could be political, environmental, or social. They deface websites, launch DDoS attacks, or leak sensitive data to the public. Remember Anonymous? Groups like that.”

Organized Crime Syndicates:
“These guys mean business. They’re after one thing: money. They’ll use everything from custom malware to phishing scams to get in. These syndicates have massive resources and know how to exploit vulnerabilities.”

Nation-state Actors:
“These are the big dogs. Government-sponsored teams running Advanced Persistent Threats (APTs) to spy, disrupt, or even wage war. They might target the Diamond if there’s something of national interest hidden here—say, money laundering records or VIP political connections.”

Insider Threats:
“The riskiest kind of attacker is the one already inside. Employees with access to key systems who might be driven by financial gain, revenge, or just plain carelessness. Even unapproved Shadow IT projects—those rogue apps or personal devices employees bring in—create holes in the network.”

Attack Paths: Threat Vectors and Attack Surfaces
Lester gestured toward the casino entrance. “Here’s the real battleground. The threat vectors—how attacks happen—and the attack surface—where they can happen.”

Message-based Vectors:
“Phishing emails pretending to be casino IT. Simple but effective.”

Image-based Vectors:
“Malicious code hidden in images sent to employees. Open the image, and bam—system compromised.”

File-based Vectors:
“Fake spreadsheets, PDFs, or software updates that deliver malware. Attachments are always dangerous.”

Voice Calls (Vhishing):
“Social engineers tricking employees over the phone into giving up credentials. Smooth talkers are a bigger threat than you think.”

Removable Devices:
“Think of a malware-infected USB drive left in the staff parking lot. An employee plugs it in out of curiosity, and suddenly the whole network’s infected. Classic baiting.”

Unsecured Networks:
“Wi-Fi hotspots in the casino can be intercepted if they’re not locked down. Even Bluetooth vulnerabilities—like BlueBorne or BlueSmack—could give attackers a way in.”

Deception and Disruption: Fighting Fire with Fire
Lester swiped to a new slide showing fake systems and traps. “To stop attackers, the casino employs deception and disruption technologies. Think of these as digital traps.”

Honeypots:
“Decoy systems designed to lure attackers. They make hackers think they’ve hit the jackpot, but really, they’re just wasting time.”

Honeynets:
“A whole network of honeypots to simulate a real system. This lets security teams study an attacker’s moves in detail.”

Honeyfiles:
“Fake files planted to detect unauthorized access. If someone opens one of these, alarms go off.”

Honeytokens:
“Dummy data that alerts admins the second it’s accessed. It’s like marking bait with invisible ink.”

Bogus DNS Entries and Decoy Directories:
“Fake domain names and folders confuse automated attacks and make hackers waste resources.”

The Threat of Shadow IT
Lester glanced at his crew. “And don’t forget the Shadow IT problem—rogue software, apps, or personal devices employees bring into the workplace without approval. These create vulnerabilities that even the best security systems can’t account for.”

Final Thoughts
Lester looked up from his tablet, his expression grim. “The Diamond’s not just a casino; it’s a battlefield. Every piece of technology, every process, and every employee is a potential weak spot. But remember: we’re not the only ones eyeing this place. The Diamond’s defenses aren’t just against us—they’re against a world of threat actors trying to take them down every day. The better we understand them, the better chance we have of outsmarting them. --""")
    print("This Is The Content Section ")
    input("Press Enter To Return To The Menu")

def vocabulary2():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "Threat Actors": "Entities that pose cybersecurity risks by attempting unauthorized actions or attacks on systems",
        "(Threat Actor Motivation) Data Exfiltration": "Unauthorized transfer of data from a computer or network",
        "(Threat Actor Motivation) Blackmail": "Obtaining sensitive or compromising information and threatening to release it unless demands are met",
        "(Threat Actor Motivation) Espionage": "Spying on individuals, organizations, or nations to gather sensitive or classified information",
        "(Threat Actor Motivation) Service Disruption": "Disrupting the services of organizations, often for chaos, ransom, or political statements",
        "(Threat Actor Motivation) Financial Gain": "Using cyberattacks to obtain monetary benefits (e.g., ransomware, banking trojans)",
        "(Threat Actor Motivation) Philosophical/Political Beliefs": "Cyberattacks motivated by ideological reasons, often tied to hacktivism",
        "(Threat Actor Motivation) Ethical Reasons": "Actions by ethical hackers aiming to improve security rather than cause harm",
        "(Threat Actor Motivation) Revenge": "Cyberattacks carried out against entities as retaliation for perceived wrongdoing",
        "(Threat Actor Motivation) Disruption/Chaos": "Creating instability by launching attacks such as malware or infrastructure disruptions",
        "(Threat Actor Motivation) War": "Cyberattacks aimed at disrupting a nation's infrastructure or compromising national security",
        "(Threat Actor Attributes) Internal Threat Actors": "Individuals or entities within an organization posing security risks",
        "(Threat Actor Attributes) External Threat Actors": "Individuals or groups outside an organization attempting to breach its cybersecurity",
        "Script Kiddies": "Unskilled attackers who use pre-made tools or scripts for hacking",
        "Hacktivists": "Individuals or groups using cyber techniques to promote political or social causes",
        "Organized Crime": "Well-structured groups conducting cyberattacks for financial gain",
        "Nation-state Actor": "Government-sponsored groups conducting cyber operations for espionage or warfare",
        "Insider Threats": "Cybersecurity threats originating from within an organization",
        "Shadow IT": "Use of IT systems, devices, software, or services without explicit organizational approval",
        "Threat Vectors": "Means or pathways attackers use to gain unauthorized access to systems",
        "Attack Surfaces": "All points where an unauthorized user can try to access or extract data",
        "Message-based Threats": "Attack vectors delivered via email, SMS, or instant messaging",
        "Image-based Threats": "Embedding malicious code inside image files to exploit systems",
        "File-based Threats": "Using disguised malicious files to infect systems (e.g., fake documents or software)",
        "Vhishing (Voice Phishing)": "Using voice calls to trick victims into revealing sensitive information",
        "Removable Devices": "Threats introduced by infected physical devices like USB drives (e.g., baiting)",
        "Unsecured Networks": "Poorly secured wireless, wired, or Bluetooth networks vulnerable to attacks",
        "BlueBorne": "Bluetooth exploit allowing attackers to take over devices or intercept communications",
        "BlueSmack": "Denial of Service (DoS) attack targeting Bluetooth-enabled devices",
        "Honeypots": "Decoy systems designed to attract and deceive attackers",
        "Honeynets": "Networks of honeypots mimicking real systems to observe attackers' methods",
        "Honeyfiles": "Decoy files placed within systems to detect unauthorized access",
        "Honeytokens": "Fake data used to alert administrators when accessed or used",
        "Bogus DNS Entries": "Fake domain names inserted into DNS servers to mislead attackers",
        "Decoy Directories": "Fake folders and files placed within a system to confuse attackers",
        "Dynamic Page Generation": "Fake pages to mislead automated scraping tools or bots",
        "Port Triggering": "Hiding services by only opening ports after detecting specific traffic patterns",
        "Fake Telemetry Data": "Sending false system or network information to mislead attackers",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

####################################################################

def submenu3():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section3()
        elif choice == "2":
            vocabulary3()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section3():
    print("\n-- Content Section --")
    type_out(""" Lester Crest stood in front of the Diamond Casino’s service entrance, gesturing toward the building with his cane. His tablet displayed a heatmap of the casino’s physical defenses: entry points, camera locations, and guard patrols.

“Alright, crew,” Lester began, adjusting his glasses. “The Diamond Casino isn’t just a fortress of cyber defenses. Its physical security measures are no joke. They’ve built this place to keep out everyone from low-level grifters to people like us. If we’re going to pull this off, we need to understand every trick they’ve got—and figure out how it’s stopping us from getting to that vault.”

Access Control Measures
Lester pointed to the casino’s main entrance. “Let’s start with access control. Getting in isn’t as simple as walking through the front door.”

Access Control Vestibule: “You see that double-door system at the main entrance? Only one door opens at a time, and you can bet it’s rigged with pressure sensors and badge readers. If you don’t have authorized credentials, you’re not getting in.”
Security Controls
Lester moved closer to the perimeter, nodding toward the barriers around the building. “The casino uses every kind of security control to slow down, deter, or completely stop intruders.”

Fencing: “They’ve got decorative fencing around the outside, but don’t let the fancy design fool you. It’s sturdy enough to stop anyone from scaling it without making a scene.”

Bollards: “See those short, steel posts near the entrances? Those are bollards, and they’re designed to stop vehicle ramming attacks. A truck isn’t getting through there.”

Door Locks: Lester tapped on his tablet, showing a breakdown of the locking mechanisms used throughout the casino.

Padlocks: “Cheap and basic, but you might see them on outdoor maintenance sheds. Still, they’re easy to break or pick.”
Biometric Locks: “High-tech stuff—fingerprint scanners, facial recognition, maybe even retinal scans. No biometrics, no entry.”
Numeric Locks: “Code-based locks. Staff might know the codes, but they’re probably rotated frequently.”
Wireless Locks: “These use NFC or RFID, and they’re tied to access badges. No signal, no access.”
Cipher Locks: “Mechanical push-button locks. Not as high-tech, but just as effective if you don’t know the combo.”
Surveillance Systems
Lester motioned toward a security camera mounted on the building’s corner. “Surveillance is where the Diamond really shines. These cameras are everywhere, and they’re equipped with all the latest features.”

Video Surveillance:

Motion Detection: “Cameras track movement and flag unusual activity.”
Night Vision: “Perfect for keeping an eye on things even in pitch darkness.”
Facial Recognition: “If you’ve got a criminal record—or just look suspicious—they’ll know.”
PTZ (Pan-Tilt-Zoom) Cameras: “These can rotate and zoom in on specific targets. If you think you’re safe just because you’re outside their immediate range, think again.”
Lighting: “Proper lighting isn’t just for aesthetics. It’s placed strategically to eliminate blind spots and enhance visibility for cameras and guards. No shadows, no hiding.”

Sensor-Based Defenses
Lester nodded toward the staff entrance. “Beyond the locks and cameras, they’ve got sensors to catch anyone trying to sneak in.”

Infrared Sensors: “Detect body heat. You can’t hide from these unless you’re invisible.”
Pressure Sensors: “Trigger alarms if they detect unexpected weight—like someone stepping where they shouldn’t.”
Microwave Sensors: “These send out waves and detect motion. Subtle but effective.”
Ultrasonic Sensors: “Measure sound wave reflections. You make a move, they know.”
Security Guards
Lester smirked. “And then there are the good old-fashioned security guards. These guys patrol the casino floor, the perimeter, and the restricted areas.”

Roles: “They’re not just there to look intimidating. Guards watch for suspicious behavior, monitor security feeds, and respond to any alarms.”
Visual Deterrence: “Their presence alone is supposed to discourage casual thieves. But we’re not casual, are we?”
Access Badges
Lester pulled a small RFID reader from his pocket. “Most employees here use access badges to move between restricted areas. These things aren’t foolproof, but they add another layer of security.”

RFID (Radio-Frequency Identification): “Contactless badges are scanned at doors for authentication.”
NFC (Near Field Communication): “Short-range communication tech. If you don’t have the right badge, you’re not getting through.”
Badge Cloning: “The casino knows this is a risk, so they monitor for suspicious activity—like someone trying to use a cloned badge.”
Common Physical Attacks
Lester turned serious, pacing in front of the crew. “Now, let’s talk about what they’re protecting against. These physical attacks are what their defenses are designed to stop.”

Brute Force Attacks:

Forcible Entry: “Breaking doors, smashing windows, or ramming barriers. That’s why they’ve got bollards, reinforced doors, and laminated glass.”
Tampering with Security Devices: “Cutting wires or disabling cameras. They’ll know immediately if something’s been tampered with.”
Ramming Barriers: “Using a vehicle to smash through gates. Those bollards will stop that cold.”
Piggybacking and Tailgating:

Piggybacking: “An authorized employee knowingly lets someone else in. It happens, but they monitor for it.”
Tailgating: “An unauthorized person sneaks in behind an authorized one. Guards are trained to watch for this.”
Bypassing Physical Security
Lester sighed and gestured toward the casino’s rooftop. “Even with all this, there are ways to bypass these defenses—if you know what you’re doing.”

Visual Obstruction: “Blocking a camera’s view with something simple, like tape or paint.”
Blinding Sensors: “Using a bright light to overwhelm cameras or infrared sensors.”
Electromagnetic Interference (EMI): “Jamming RFID signals or disrupting surveillance systems. They’ve probably hardened their equipment against this.”
Tampering: “Physically disabling locks, sensors, or cameras. But good luck doing that without triggering an alarm.”
Lester turned back to the crew, his voice sharp and commanding. “You see what we’re up against? This isn’t just about hacking the vault or bribing some low-level employee. The Diamond has built layer upon layer of physical security to stop people like us. If we want that payout, we need to think smarter and faster than their systems.”

He smirked. “And trust me, I’ve already got a few ideas. Now let’s get to work.”

The crew nodded, ready to dive into the details of the heist, knowing full well they were taking on a fortress built to keep them out. """)
    input("Press Enter To Return To The Menu")

def vocabulary3():
    print("\n-- Vocabulary ---") ###fix comments into brackets 
    vocabulary_dict = {
        "Physical Security": "Measures to protect tangible assets (buildings, equipment, people) from harm or unauthorized access",
        "Access Control Vestibule": "A double-door system allowing only one door to be open at a time, preventing unauthorized access",
        
        # Security Controls
        "Fencing": "Barriers enclosing areas to define boundaries and delay intruders",
        "Bollards": "Short, sturdy vertical posts to control or prevent vehicle access",
        "Padlocks": "Basic external locks, easily defeated",
        "Biometric Locks": "Use fingerprints, facial recognition, or retinal scans",
        "Numeric Locks": "Require entry of a code",
        "Wireless Locks": "Use NFC, Bluetooth, or RFID technology",
        "Cipher Locks": "Mechanical locks with push buttons",
        
        # Surveillance Systems
        "Video Surveillance": "Includes features like motion detection, night vision, facial recognition, and PTZ (Pan-Tilt-Zoom) cameras",
        "Lighting": "Proper lighting deters criminals and enhances visibility for cameras and guards",
        "Infrared Sensors": "Detect body heat",
        "Pressure Sensors": "Triggered by weight",
        "Microwave Sensors": "Detect motion through emitted waves",
        "Ultrasonic Sensors": "Measure sound wave reflections",
        "Security Guards": "Provide visual deterrence and monitor activities",
        
        # Access Badges
        "RFID (Radio-Frequency Identification)": "Contactless authentication technology",
        "NFC (Near Field Communication)": "Enables short-range communication for access control",
        "Badge Cloning": "Copying access badge data to gain unauthorized entry",
        
        # Common Physical Attacks
        "Brute Force Attacks": "Forcible entry by breaking doors, windows, or barriers",
        "Tampering with Security Devices": "Manipulating or disabling cameras and sensors",
        "Ramming Barriers": "Using vehicles to breach security gates",
        "Piggybacking": "Authorized user knowingly lets an unauthorized person enter",
        "Tailgating": "Unauthorized person sneaks in behind an authorized user without consent",
        
        # Bypassing Physical Security
        "Visual Obstruction": "Blocking a camera’s view with objects, paint, or tape",
        "Blinding Sensors": "Using bright light to overwhelm cameras or sensors",
        "Electromagnetic Interference (EMI)": "Jamming signals used by surveillance systems",
        "Tampering": "Physically disabling or destroying security devices",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

 #####################################################################################################       

def submenu4():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section4()
        elif choice == "2":
            vocabulary4()
        elif choice =="3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()                     

def content_section4():
    print("\n-- Content Section --")
    type_out(""" The team gathered in the planning room as Lester Crest paced back and forth, his tablet clutched in one hand. He stopped and looked up, a sly grin creeping across his face.

“Alright, now that you understand the physical security of the Diamond,” he began, “it’s time to talk about social engineering. Physical barriers and tech can stop a brute-force attack, but the casino’s greatest vulnerability isn’t its locks or cameras—it’s the people running the place. Humans are always the weakest link.”

Lester pulled up a digital profile of a Diamond Casino employee on his tablet. “To break into this fortress, we’re not just going to outsmart their systems. We’re going to manipulate the people who work here to open the doors for us.”

The Basics of Social Engineering
“Social engineering is about using human psychology to get what we want. The casino staff won’t even realize they’re helping us. Here are the psychological motivational triggers we’ll exploit.”

Authority:
“If you act like you’re in charge, most people won’t question you. Wear a maintenance uniform, carry a clipboard, and you’re practically invisible.”

Urgency:
“Creating a sense of urgency makes people panic. Imagine telling the manager that the vault security system is about to malfunction unless they let you in to ‘fix’ it.”

Social Proof:
“People follow the crowd. If they think ‘everyone else is doing it,’ they’ll do it too. We can use that to manipulate staff into ignoring protocol.”

Scarcity:
“Convince them they’re about to miss out on something—like a last-minute cash drop or a time-sensitive repair—and they’ll bend the rules to help.”

Likability:
“Be charming, friendly, and relatable. People are more likely to trust someone they like.”

Fear:
“When all else fails, scare them. A threat of a system failure or an audit can force people to act without thinking.”

Social Engineering Techniques
Lester moved to the whiteboard, sketching out potential scenarios. “Now let’s talk about the techniques we’ll use to manipulate these people.”

Impersonation:
“Pretend to be someone they trust—a technician, a delivery driver, even another employee. The Diamond’s staff aren’t going to stop someone who looks like they belong.”

Pretexting:
“Create a believable story to get them to spill sensitive information. For example, call the security desk claiming to be IT and ask for their login credentials to ‘fix an issue.’”

Baiting:
“Leave a malware-laden USB drive lying around with a label like ‘Payroll Info’ or ‘Confidential.’ Someone’s going to plug it into a computer out of curiosity.”

Phishing:
“Send a fake email to the casino manager, asking them to confirm their credentials to access an urgent update. Once they do, we’ve got their login info.”

Phishing Variants
Lester tapped the board to emphasize the different forms of phishing they could use.

Vishing (Voice Phishing):
“We’ll call the front desk pretending to be from the bank, asking for account verification. It’s amazing how easily people hand over sensitive details.”

Smishing (SMS Phishing):
“Send a text message claiming to be from casino management, instructing employees to click a link to ‘update’ their credentials.”

Spear Phishing:
“Highly targeted attacks. For example, we send an email to the security manager using their name and referencing specific details about the casino.”

Whaling:
“This one’s for high-level targets like the casino CEO. A well-crafted email, tailored to their responsibilities, can make them fall for a scam just as easily.”

Business Email Compromise (BEC):
“If we can compromise an employee’s email account, we can send messages directly from their address, tricking others into following our instructions.”

Frauds and Scams
Lester smirked as he brought up a list of common scams. “Casinos are constantly targeted by scams, so their staff are used to seeing them. But if we’re clever enough, they won’t see us coming.”

Identity Fraud:
“Using stolen credentials or impersonating employees to access restricted areas.”

Invoice Scam:
“Send an official-looking invoice to the casino’s accounts payable department for a fake service. If they pay it, we’re richer without even stepping inside.”

Other Social Engineering Attacks
“Let’s talk about the more direct methods,” Lester continued. “These are low-tech but highly effective.”

Diversion Theft:
“Create a distraction—like a fake fire alarm or a spilled drink—to redirect attention while we make our move.”

Hoaxes:
“Spread false information to confuse and mislead employees. For example, claim there’s a virus on the system so they call us for ‘help.’”

Shoulder Surfing:
“Stand behind someone while they’re entering a PIN or typing a password. Subtle, but effective.”

Dumpster Diving:
“Check the trash for discarded documents or notes with passwords. You’d be surprised what people throw away.”

Eavesdropping:
“Listen to conversations in staff areas to pick up useful details—like access codes or schedules.”

Piggybacking:
“Convince an employee to let us in by pretending we forgot our badge.”

Tailgating:
“Sneak in behind someone who’s already unlocked a door. Guards are trained to stop this, but they can’t catch everything.”

Influence Campaigns
Lester’s tone grew serious. “Sometimes, you don’t need to be in the building to cause chaos. Influence campaigns can throw the casino into disarray and make it easier for us to strike.”

Misinformation:
“Spread false information unintentionally, like rumors about a fake audit or inspection.”

Disinformation:
“Deliberately spread lies to confuse or mislead. For example, tell the staff the IT department is upgrading their systems, and we’ll have them handing over passwords in no time.”

Lester’s Plan in Motion
Lester leaned on his cane, a mischievous twinkle in his eye. “This casino thinks its biggest threats are hackers or brute-force break-ins. But they’ve got hundreds of employees walking through those doors every day, and each one is a potential weakness. If we use these techniques right, we won’t just get through their defenses—we’ll make them open the doors for us.”

The crew nodded, already imagining how they’d use charm, deception, and manipulation to exploit the Diamond Casino’s human vulnerabilities. Lester grinned. “Now, who’s ready to play the long game?”

The team left the planning room, their heads full of ideas for exploiting the human side of security. Lester stayed behind, already crafting the pretexts and phishing campaigns that would make the heist a masterpiece of social engineering. """)
    input("Press Enter To Return To The Menu")

def vocabulary4():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---General Terms---"
        "Social Engineering": "Manipulating human psychology to gain unauthorized access to systems, data, or physical spaces",
        "Motivational Triggers": "Psychological tactics used to influence targets",
        "Authority": "Using perceived power to compel compliance",
        "Urgency": "Creating a sense of time pressure",
        "Social Proof": "Influencing based on others' actions",
        "Scarcity": "Leveraging limited availability to manipulate decisions",
        "Likability": "Building rapport to gain trust",
        "Fear": "Threatening negative consequences to push action",

        "---Social Engineering Techniques---"
        "Impersonation": "Pretending to be someone else to gain trust or access",
        "Pretexting": "Fabricating scenarios to elicit sensitive information",
        "Baiting": "Leaving enticing, malware-laden devices (e.g., USB drives) to trap victims",
        "Phishing": "Fraudulent attempts to steal sensitive information through deceptive emails",

        "---Types of Phishing Attacks---"
        "Vishing": "Voice phishing via phone calls",
        "Smishing": "SMS phishing via text messages",
        "Spear Phishing": "Targeted phishing aimed at specific individuals or groups",
        "Whaling": "High-profile spear phishing targeting executives (e.g., CEOs, CFOs)",
        "Business Email Compromise (BEC)": "Using compromised business accounts to manipulate employees",

        "---Frauds and Scams---"
        "Identity Fraud": "Using personal information for financial or personal gain",
        "Invoice Scam": "Tricking victims into paying fake invoices",

        "---Other Social Engineering Attacks---"
        "Diversion Theft": "Creating distractions to steal assets",
        "Hoaxes": "Spreading false information to deceive victims",
        "Shoulder Surfing": "Observing someone’s screen or keyboard to steal information",
        "Dumpster Diving": "Retrieving sensitive data from discarded materials",
        "Eavesdropping": "Secretly listening to private conversations",
        "Piggybacking": "Authorized user knowingly allows unauthorized entry",
        "Tailgating": "Unauthorized user follows an authorized one without consent",

        "---Influence Campaigns"
        "Misinformation": "Sharing false information unintentionally",
        "Disinformation": "Deliberately spreading false information to mislead",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

 #####################################################################################################

def submenu5():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section5()
        elif choice == "2":
            vocabulary5()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()                     

def content_section5():
    print("\n-- Content Section --")
    type_out(""" “You know,” he began, “physical security and social engineering are just the appetizers. If we really want to hit the Diamond where it hurts, we need to talk about malware. This isn’t just about breaking into vaults anymore; this is about planting seeds in their systems to wreak havoc later.”

Understanding Malware in the Casino's Context
Lester projected a schematic of the casino’s IT infrastructure onto the wall. "The Diamond’s network is a digital fortress, but even the strongest walls can crumble when you introduce the right kind of pest. Let’s break it down.”

Viruses:

"A virus is like the common cold for computers. It attaches itself to clean files, spreads, and corrupts host files. Imagine slipping one into the casino's customer service system—soon enough, it’s everywhere."
Worms:

“Worms are the viruses’ overachieving cousins. They don’t need help to spread; they replicate themselves and move from one system to another, saturating network bandwidth. One worm in the surveillance network, and their cameras start going haywire.”
Trojans:

"The classics—Trojans. They look like legitimate software but open the door for us. Picture a fake security patch sent to their IT team. They install it, and boom—we have access."
Ransomware:

“Now this is the heavy hitter. Ransomware encrypts their data and demands payment. Lock up their payroll records, and suddenly, no one’s getting paid unless they cough up cash—or give us a way in.”
Spyware:

"Then there’s spyware. We drop it onto a receptionist’s workstation, and it starts logging keystrokes, collecting passwords, and feeding us their secrets."
Rootkits:

“A rootkit is what we’d use for persistence. Once it’s in, it hides itself and gives us administrative-level access to their systems. They won’t even know we’re there.”
How Malware Could Affect the Casino
Lester moved to another schematic, this one focused on casino operations.

Surveillance System Disruption:

“A well-placed worm could overload their network, taking down surveillance cameras or creating blind spots.”
Access Control Bypass:

“Using a trojan to plant a backdoor in their access control system could let us override badge requirements and waltz in undetected.”
Financial System Chaos:

"Injecting ransomware into their accounting software would grind all transactions to a halt. They wouldn’t be able to reconcile payouts or even process high roller deposits."
Operational Lockdown:

“If their slot machines or gaming tables run on connected systems—and they do—a virus could crash the whole floor. Pandemonium is good cover for us.”
Data Theft:

“Spyware could grab personal details from VIP customers. Blackmail material or just a distraction—either works in our favor.”
Infection Vectors
Lester pointed to the casino's email server on the schematic. "The Diamond has a few potential vulnerabilities we could exploit."

Unpatched Software:

"Their systems rely on regular updates, but no IT team is perfect. Find an unpatched vulnerability, and we’re in."
USB Baiting:

"A classic move. Leave a malware-laden USB drive labeled ‘Jackpot Records’ in the breakroom. Someone will plug it in.”
Phishing Emails:

"Disguising ourselves as the casino’s IT team, we could send an email with a fake update. One click, and their network is ours."
Signs of Malware Defenses
Lester sighed, his smirk fading slightly. “Of course, they’re not clueless. They’ve got defenses too.”

Endpoint Protection:

"Antivirus and antimalware software will scan for known threats. We’ll need to make anything we use look benign."
Intrusion Detection Systems (IDS):

"These monitor for unusual activity, like an unexpected spike in network traffic. The moment we’re too loud, they’ll know."
File Integrity Monitoring:

"Changes to critical files are flagged. If we tamper with the access control database, it better look clean."
System Logs:

“Everything we do leaves traces—if we’re not careful, they’ll find them in the logs.”
Key Challenges
Before concluding, Lester laid out the primary hurdles the team would face.

Detection Avoidance:

“If the casino's systems flag our malware, the game’s over before it starts.”
Containment Measures:

"Their IT team will isolate infected systems as soon as something looks wrong. We’ll need to strike fast."
Incident Response Teams:

"The Diamond probably has a dedicated team trained to counter cyberattacks. Once they’re on high alert, they’ll shut down entry points one by one."
Lester leaned back, his voice low but determined. “This isn’t just about outsmarting a system—it’s about slipping through the cracks without anyone knowing we were there. That’s the real art. So, are you all ready to learn how to think like malware?”

The team exchanged nervous glances, knowing they were heading into uncharted territory. Lester smiled. “Good. Let’s make some chaos.” """)
    input("Press Enter To Return To The Menu")

def vocabulary5():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Malware Types---"
        "Virus": "Malware that attaches itself to a host file, spreading and corrupting files when executed.",
        "Worm": "Malware that self-replicates and spreads across networks without needing a host file.",
        "Trojan": "Malware disguised as legitimate software to trick users into installing it, often creating a backdoor.",
        "Ransomware": "Malware that encrypts files and demands payment to unlock them.",
        "Spyware": "Malware that secretly collects data, such as passwords and keystrokes, from an infected system.",
        "Rootkit": "Malware that hides itself and provides unauthorized administrative-level access to the system.",
        
        "---Infection Vectors---"
        "Unpatched Software": "Software with known vulnerabilities that can be exploited by attackers if not updated.",
        "USB Baiting": "A social engineering attack where malware-laden USB drives are left in public areas to trick people into plugging them into computers.",
        "Phishing Emails": "Emails designed to trick recipients into clicking malicious links or downloading malware.",
        
        "---Malware Effects---"
        "Surveillance System Disruption": "Using malware to overload or disable surveillance systems, creating blind spots.",
        "Access Control Bypass": "Injecting malware into access control systems to override restrictions and gain unauthorized entry.",
        "Financial System Chaos": "Introducing malware to disrupt financial systems, preventing transactions or payouts.",
        "Operational Lockdown": "Using malware to crash operational systems, such as slot machines or gaming tables, causing widespread disruption.",
        "Data Theft": "Using malware to steal sensitive information, such as customer details or employee credentials.",
        
        "---Malware Defenses---"
        "Endpoint Protection": "Software like antivirus and antimalware tools designed to detect and remove threats.",
        "Intrusion Detection Systems (IDS)": "Systems that monitor for unusual or malicious activity within a network.",
        "File Integrity Monitoring": "Tools that flag changes to critical files, helping detect tampering or unauthorized access.",
        "System Logs": "Records of system activities that can be analyzed to detect signs of malware or suspicious behavior.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu6():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section6()
        elif choice == "2":
            vocabulary6()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section6():
    print("\n-- Content Section --")
    type_out(""" They’re not just guarding money; they’re guarding information—records, transactions, VIP client lists, employee details, you name it. That data is worth just as much as what’s in the vault.”

Understanding the Diamond’s Data
Lester walked over to the board and scribbled the word “DATA” in big letters.

“Think of data as the casino’s lifeblood. If their systems crash, or their secrets get out, they’re toast. That’s why they’ve built layers of protection to keep it safe. Here’s what they’re doing and why it makes our job harder.”

Encryption:

“The first line of defense. All sensitive data—client records, surveillance logs, financial transactions—is encrypted. That means it’s scrambled into meaningless gibberish unless you have the decryption key. Without that key, we’re blind.”
Access Controls:

“Not everyone in the casino has access to the same data. High-ranking staff get full access, while janitors only see the cleaning schedule. These controls are fine-tuned to prevent anyone from snooping around where they shouldn’t.”
Data Masking:

“Even when data is shared internally, it’s masked to hide sensitive parts. For example, a staff member might see the last four digits of a customer’s credit card, but not the whole thing.”
Backups:

“They’ve got redundant backups stored offsite, both digitally and physically. Even if we wipe their systems clean, they’ll have copies ready to restore.”
Data Loss Prevention (DLP):

“Their DLP systems monitor for unusual data movement—like someone emailing sensitive files or downloading too much at once. If anything seems suspicious, alarms go off.”
Data Protection Policies
Lester switched slides, revealing a list of the casino’s likely policies.

“They don’t just rely on tech. Policies keep their people in line, and breaking these rules probably gets you fired.”

Least Privilege Principle:

“Employees only get access to the data they absolutely need. No extra permissions, no exceptions.”
Regular Audits:

“They go through logs regularly, checking for unauthorized access or suspicious behavior.”
Retention Policies:

“Old data gets deleted or archived according to strict timelines. No point hacking into an account that’s been inactive for years—it won’t have anything useful.”
Challenges Posed by Data Protection
Lester leaned on his cane and scanned the group. “Now let’s talk about how all this makes our job harder.”

Encrypted Vault Records:

“Even if we grab the vault schedule or codes, it’ll be encrypted. Without the decryption key, it’s useless.”
Access Restrictions:

“Say you bribe a low-level employee. They won’t have the permissions to give you what you need.”
DLP Systems:

“If we try to copy too much data at once, or send it out of their network, their systems will flag it.”
Backups:

“Even if we crash their systems, they’ll recover. We’d have to hit both the live data and the backups simultaneously.”
Potential Weak Points
Lester smirked, flipping to a diagram of the casino’s data infrastructure. “Of course, every fortress has its cracks. Here’s what we could exploit.”

Insider Knowledge:

“An IT staffer with access to the encryption keys is worth their weight in gold. We find one, and we’re halfway there.”
Human Error:

“Even the best systems are run by fallible humans. Someone forgets to mask a file, clicks the wrong button, or leaves sensitive info lying around? That’s our window.”
Old Systems:

“Parts of their network might run on outdated software. A legacy system could have vulnerabilities we can exploit.”
Misconfigured DLP Rules:

“If their data loss prevention rules aren’t set up properly, we could move data around without triggering alarms.”
Data Protection Tools
Lester zoomed in on a list of security tools the casino likely uses. “And here are the tools they’re using to keep us out.”

Encryption Algorithms:

“AES-256, RSA—you name it. These algorithms are tough to crack without the key.”
Multi-Factor Authentication (MFA):

“Even if we get someone’s password, we’ll need their second factor—like a mobile code or biometric scan.”
Monitoring Tools:

“SIEM systems (Security Information and Event Management) track everything. Unusual access patterns? Flagged.”
Firewalls:

“Their firewalls will block any attempt to access their systems from unauthorized devices.”
Lester’s Closing Thoughts
Lester turned back to the crew, his expression calm but serious. “The Diamond Casino knows how valuable its data is. They’ve invested heavily in keeping it safe—and for good reason. If we want to crack this, we need to be smarter than their policies, faster than their systems, and one step ahead of their IT team.”

He paused, letting the weight of the challenge settle over the group. Then, with a gleam in his eye, he added, “But hey, who doesn’t love a good puzzle?”

The crew exchanged determined nods, ready to tackle the digital fortress standing between them and the prize. """)
    input("Press Enter To Return To The Menu")

def vocabulary6():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Data Protection Basics---"
        "Encryption": "The process of converting data into a coded form to prevent unauthorized access.",
        "Access Controls": "Mechanisms that restrict access to data based on user permissions.",
        "Data Masking": "The process of hiding sensitive parts of data, such as showing only the last four digits of a credit card.",
        "Backups": "Redundant copies of data stored digitally or physically to recover from data loss.",
        "Data Loss Prevention (DLP)": "Systems that monitor and prevent unauthorized movement or sharing of sensitive data.",
        
        "---Data Protection Policies---"
        "Least Privilege Principle": "The policy of granting users only the access necessary for their job duties.",
        "Regular Audits": "The process of reviewing system logs and activity to identify unauthorized access or suspicious behavior.",
        "Retention Policies": "Rules for how long data is stored before it is deleted or archived.",

        "---Challenges of Data Protection---"
        "Encrypted Vault Records": "Sensitive data that is stored in an encrypted format, requiring a decryption key to access.",
        "Access Restrictions": "Limitations that prevent users without the correct permissions from viewing certain data.",
        "Data Loss Prevention Systems (DLP)": "Systems that flag suspicious data movement, such as large file downloads or unauthorized transfers.",
        "Backups and Recovery": "Processes to restore data from copies in case of system failure or attack.",

        "---Potential Weak Points---"
        "Insider Knowledge": "Sensitive information that can be exploited, often obtained from employees with access privileges.",
        "Human Error": "Mistakes made by individuals that can compromise security, such as forgetting to mask sensitive data.",
        "Old Systems": "Outdated technology with vulnerabilities that can be exploited by attackers.",
        "Misconfigured DLP Rules": "Improperly set up data loss prevention systems that fail to detect suspicious activity.",

        "---Tools for Data Protection---"
        "Encryption Algorithms": "Mathematical formulas like AES-256 or RSA used to secure data.",
        "Multi-Factor Authentication (MFA)": "An authentication method that requires multiple forms of verification, such as a password and a mobile code.",
        "Monitoring Tools": "Systems like SIEM that track user activity and flag unusual behavior.",
        "Firewalls": "Security tools that block unauthorized access to networks or systems.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu7():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section7()
        elif choice == "2":
            vocabulary7()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section7():
    print("\n-- Content Section --")
    type_out(""" Lester leaned back in his chair, rubbing his temples as the crew murmured amongst themselves. The tension in the room was palpable as the conversation turned to the vault’s ultimate security layer. He tapped his tablet, and the display shifted to a list of encryption protocols and algorithms.

“Alright, listen up,” Lester said sharply, his eyes scanning the room. “The Diamond Casino doesn’t just rely on locks and cameras. Their most precious data—vault codes, employee credentials, customer transactions—it’s all protected by cryptographic solutions. These aren’t just walls. They’re digital fortresses.”

Understanding Cryptographic Layers
Lester walked to the whiteboard and scribbled the word "CRYPTOGRAPHY" in bold letters.

“Cryptography is the art of securing data,” he explained. “It ensures that even if we intercept something—like vault passcodes—it’ll be completely useless without the decryption key. Here’s what we’re dealing with.”

Symmetric Encryption:

“Both encryption and decryption use the same key. Think of it like a shared secret. The good news? If we can get that key, we’re golden. The bad news? They keep those keys locked tighter than the vault itself.”
Asymmetric Encryption:

“This one’s trickier. It uses two keys: a public key to encrypt and a private key to decrypt. Even if we get the public key, it’s useless without the private one. The casino uses this for secure communications, like transferring sensitive data to their offsite backup systems.”
Hashing:

“This isn’t encryption—it’s one-way obfuscation. The vault system probably hashes employee PINs. We can’t reverse a hash, but if we know what the input is, we can match it to the hash.”
Digital Signatures:

“Every transaction in their systems is authenticated with a digital signature. If we tamper with anything, the system will know because the signature won’t match.”
Cryptographic Protocols at the Casino
Lester swiped to a slide showing the casino’s likely cryptographic protocols. “These are the tools they’re using to keep us out.”

TLS (Transport Layer Security):

“This ensures all data transmitted over the casino’s network—whether it’s credit card payments or vault access logs—is encrypted. Even if we intercept it, we won’t be able to read it.”
PKI (Public Key Infrastructure):

“They’re using this for asymmetric encryption. PKI manages their public and private keys, ensuring secure communication between devices.”
AES (Advanced Encryption Standard):

“The gold standard for symmetric encryption. It’s fast, efficient, and nearly impossible to crack without the key.”
RSA:

“This is their go-to for asymmetric encryption. It’s used for secure logins and transmitting sensitive data.”
How Cryptography Stops Us
Lester leaned on his cane, his tone grim. “Here’s why this is a nightmare for people like us.”

Data in Transit:

“Even if we intercept data moving through their network, it’ll be encrypted. Without the keys, it’s just gibberish.”
Data at Rest:

“Vault codes, employee credentials, and customer information are stored in an encrypted format. Breaking that encryption isn’t an option.”
Integrity Checks:

“Hashing ensures the data hasn’t been tampered with. If we try to alter it, the hash won’t match, and alarms will go off.”
Authentication:

“Every time someone logs into their systems, the casino uses asymmetric encryption to verify their identity. There’s no way to spoof that without their private keys.”
Potential Weak Points
Lester smirked, tapping his tablet. “Of course, even the best systems have weaknesses.”

Key Management:

“The encryption is only as strong as the keys. If we can access their key management server or steal a private key, we’re in.”
Human Error:

“An employee might reuse passwords, leave private keys on an insecure workstation, or fall for a phishing scam. That’s our opening.”
Outdated Protocols:

“If they’re using older cryptographic protocols—like outdated versions of RSA or TLS—we might be able to exploit known vulnerabilities.”
Side-Channel Attacks:

“We don’t have to crack the encryption directly. If we can monitor their system’s behavior—like timing or power usage—we might infer the keys.”
Cryptographic Tools in Action
Lester gestured toward the projected slide. “Here’s what they’re using to lock us out—and what we might be able to twist to our advantage.”

Key Escrow:

“Some of their keys might be stored with third-party escrow services. If we can compromise the escrow, we’ll get access.”
Certificate Authorities:

“Their PKI relies on trusted certificate authorities. If we spoof one of these, we can intercept their encrypted traffic.”
HSM (Hardware Security Module):

“This is where they store encryption keys. Breaking into an HSM is almost impossible—but nothing’s truly unbreakable.”
Two-Factor Authentication (2FA):

“It’s not strictly cryptographic, but 2FA relies on cryptographic algorithms to generate time-sensitive codes. If we can intercept those codes, we’re golden.”
Lester’s Plan for Cryptography
Lester turned back to the crew, his eyes gleaming with determination. “The Diamond Casino thinks cryptography makes them invincible. But cryptography isn’t magic—it’s just math. And like any system, it’s only as strong as its weakest link. We’re going to find that link, exploit it, and turn their fortress into our playground.”

The crew exchanged wary glances, knowing the heist was growing more complex by the minute. Lester chuckled. “Don’t worry. I wouldn’t lead you into this if I didn’t know we could win. Now, let’s get cracking—literally.”

With that, he spun around, already sketching out the next step in their plan. The heist was becoming a masterpiece, one cryptographic layer at a time. """)
    input("Press Enter To Return To The Menu")

def vocabulary7():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Cryptographic Basics---"
        "Symmetric Encryption": "Encryption where the same key is used for both encrypting and decrypting data.",
        "Asymmetric Encryption": "Encryption that uses a public key for encryption and a private key for decryption.",
        "Hashing": "A one-way process that converts data into a fixed-length value for verifying integrity.",
        "Digital Signatures": "Cryptographic tools used to verify the authenticity and integrity of a message or document.",

        "---Cryptographic Protocols---"
        "TLS (Transport Layer Security)": "Protocol that ensures encrypted communication over a network.",
        "PKI (Public Key Infrastructure)": "System that manages public and private keys for secure communication.",
        "AES (Advanced Encryption Standard)": "A symmetric encryption standard used for securing sensitive data.",
        "RSA": "An asymmetric encryption algorithm used for secure data transmission.",

        "---Challenges in Cryptography---"
        "Data in Transit": "Data being transmitted across a network, protected by encryption.",
        "Data at Rest": "Data stored in an encrypted format to prevent unauthorized access.",
        "Integrity Checks": "Mechanisms to verify that data has not been tampered with, often using hashing.",
        "Authentication": "The process of verifying the identity of a user or system, often through encryption.",

        "---Potential Weak Points---"
        "Key Management": "The process of securely handling encryption keys, critical to maintaining security.",
        "Human Error": "Mistakes made by individuals, such as poor password practices or mishandling keys.",
        "Outdated Protocols": "Old encryption methods that may have known vulnerabilities.",
        "Side-Channel Attacks": "Attacks that exploit indirect information, like timing or power usage, to infer cryptographic keys.",

        "---Cryptographic Tools---"
        "Key Escrow": "A system where encryption keys are stored with a trusted third party for backup.",
        "Certificate Authorities": "Entities that issue and manage digital certificates in a PKI system.",
        "HSM (Hardware Security Module)": "A physical device used to securely store encryption keys and perform cryptographic operations.",
        "Two-Factor Authentication (2FA)": "A security method that requires two forms of authentication, often involving cryptographic algorithms.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu8():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section8()
        elif choice == "2":
            vocabulary8()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section8():
    print("\n-- Content Section --")
    type_out(""" The crew had gathered once again in the dimly lit planning room. Lester Crest stood at the front, his laptop connected to the projector, displaying a diagram of the casino’s risk management framework. His voice was sharp, almost amused, as he addressed the team.

“You know, the Diamond Casino’s security isn’t just about locks, cameras, and encryption,” Lester began, gesturing at the screen. “It’s about minimizing risk—finding all the possible ways someone like us could exploit them and shutting those doors before we even get there. That’s risk management. And let me tell you, these guys take it seriously.”

Risk Management at the Diamond
Lester pointed to a risk matrix chart on the screen. “Risk management is about balancing the odds. The Diamond doesn’t just protect against what’s likely—they protect against what’s devastating. Here’s how they approach it.”

Risk Assessment:

“The first step is figuring out what can go wrong and how bad it could be. For example, losing customer data might not happen often, but when it does? Lawsuits, fines, reputational damage—it’s catastrophic.”
Threat Analysis:

“They analyze potential threats—like cyberattacks, insider sabotage, or even natural disasters. Anything that could disrupt operations or compromise their precious vault.”
Vulnerability Assessment:

“They also identify vulnerabilities—weaknesses in their systems, processes, or even people. This could be anything from unpatched software to careless employees.”
Risk Matrix:

“Once they know the threats and vulnerabilities, they use a risk matrix to categorize risks by likelihood and impact. High-impact, high-likelihood risks get the most attention.”
Risk Treatment
Lester smirked, flipping to the next slide. “But identifying risks isn’t enough. They need to deal with them. Here’s how they do it.”

Risk Avoidance:

“The simplest solution—just don’t do anything that creates the risk. For example, they don’t store vault codes in plain text anywhere. If it’s not there, we can’t steal it.”
Risk Mitigation:

“This is about reducing the likelihood or impact of a risk. They encrypt everything, implement firewalls, and conduct regular employee training. All those annoying layers of defense? That’s mitigation.”
Risk Transfer:

“This one’s clever. They transfer risk to someone else, like an insurance company. If someone does manage to rob them, they’ve got coverage.”
Risk Acceptance:

“Not every risk can be avoided, mitigated, or transferred. Sometimes, they just accept it—like the chance that a VIP customer might cheat at the tables. They monitor it but don’t spend too much money preventing it.”
Key Risk Management Tools
Lester highlighted a list of tools the casino likely uses. “To manage risks, they’ve armed themselves with some pretty advanced tools.”

Risk Registers:

“This is their ledger of all potential risks. Every threat, vulnerability, and treatment plan is logged and tracked here.”
Security Information and Event Management (SIEM):

“A SIEM system collects data from across their network, analyzes it, and flags anything suspicious. It’s their all-seeing eye.”
Business Impact Analysis (BIA):

“They use this to figure out what happens if something goes wrong. For example, how long can the casino survive if the slot machines are down?”
Incident Response Plans:

“This is their playbook for when things go south. If a risk becomes reality—like a breach or a power outage—they’ve got step-by-step plans to contain and recover.”
Risk Monitoring
Lester gestured at the risk management cycle projected on the wall. “But risk management isn’t a one-and-done deal. The casino knows risks change over time.”

Continuous Monitoring:

“They’re always watching—updating their risk assessments as new threats emerge. For example, a new malware strain? It goes straight onto their radar.”
Audits:

“Regular audits ensure their defenses are working. If a control isn’t doing its job, they replace or upgrade it.”
Lessons Learned:

“Every time something goes wrong, they analyze it. Why did it happen? How do they stop it next time?”
Challenges for Us
Lester sighed, tapping his cane on the floor. “So, what does this mean for us? It means the Diamond isn’t just reactive—they’re proactive. They’ve already thought about people like us and put measures in place to stop us.”

Overlapping Controls:

“Every risk has multiple controls. Even if we bypass one, there’s another waiting to catch us.”
Real-Time Monitoring:

“Their SIEM system can detect anomalies in real time. We can’t be sloppy—not even for a second.”
Incident Response Teams:

“The moment something feels off, they’ll deploy a team to shut it down. We’ll have to act faster than their response.”
Low Tolerance for Errors:

“The Diamond accepts almost no risks in critical areas. They spend heavily on security to ensure nothing goes wrong.”
Exploitable Weaknesses
But Lester wasn’t done. He leaned in, lowering his voice. “Of course, no system is perfect. Here’s where they might slip up.”

Complacency:

“The more risks they mitigate, the safer they feel. Overconfidence makes people lazy.”
Human Weakness:

“Their employees are still the weakest link. Even with training, someone might ignore a protocol or fall for a phishing email.”
Cost vs. Benefit:

“They might skimp on mitigating low-likelihood risks, thinking they’re safe. That’s where we strike.”
Outdated Plans:

“If they don’t update their incident response plans regularly, they’ll stumble when something unexpected happens.”
Lester’s Final Words
Lester turned to face the crew, his expression sharp and calculating. “Risk management is their game—and it’s a good one. But it has cracks. Every control they’ve put in place has a limit, and every plan has a blind spot. We find those cracks, we exploit those blind spots, and we take what’s ours.”

The crew nodded, the weight of the task settling over them. Lester grinned. “Now, let’s show the Diamond Casino that no amount of risk management can stop us.”

With that, the heist planning moved into its final stages, each member of the crew armed with the knowledge needed to outmaneuver the casino’s seemingly impenetrable defenses. """)
    input("Press Enter To Return To The Menu")

def vocabulary8():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Risk Management Basics---"
        "Risk Management": "The process of identifying, assessing, and mitigating risks to achieve organizational goals.",
        "Risk Assessment": "Evaluating potential risks by analyzing their likelihood and impact.",
        "Threat Analysis": "Identifying and understanding potential threats that could harm an organization.",
        "Vulnerability Assessment": "Examining weaknesses in systems or processes that could be exploited.",
        "Risk Matrix": "A tool that categorizes risks based on their likelihood and impact.",

        "---Risk Treatment Strategies---"
        "Risk Avoidance": "Eliminating activities that introduce risk.",
        "Risk Mitigation": "Reducing the likelihood or impact of a risk through controls or safeguards.",
        "Risk Transfer": "Shifting the risk to another party, such as an insurance provider.",
        "Risk Acceptance": "Acknowledging a risk and choosing to tolerate it without additional controls.",

        "---Risk Management Tools---"
        "Risk Register": "A document that records and tracks identified risks and their treatments.",
        "SIEM (Security Information and Event Management)": "A system that collects and analyzes security data for real-time threat detection.",
        "Business Impact Analysis (BIA)": "A process that evaluates the effects of a disruption on business operations.",
        "Incident Response Plan": "A structured approach for detecting, responding to, and recovering from security incidents.",

        "---Risk Monitoring---"
        "Continuous Monitoring": "Ongoing observation of risks to identify changes or new threats.",
        "Audits": "Systematic reviews of controls and processes to ensure they are effective.",
        "Lessons Learned": "Post-incident reviews to improve processes and prevent future risks.",

        "---Challenges and Weak Points---"
        "Overlapping Controls": "Multiple security measures addressing the same risk to ensure redundancy.",
        "Real-Time Monitoring": "Systems that detect and alert on threats as they occur.",
        "Incident Response Teams": "Specialized teams trained to handle security incidents.",
        "Human Weakness": "Mistakes or vulnerabilities caused by human behavior, such as ignoring protocols or falling for scams.",
        "Outdated Plans": "Response plans that are no longer effective due to changes in threats or systems.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

######################################################################################################

def submenu9():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section9()
        elif choice == "2":
            vocabulary9()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section9():
    print("\n-- Content Section --")
    type_out(""" “You’ve all seen how tight the Diamond’s defenses are,” he said, smirking as he adjusted his glasses. “But here’s the thing—they don’t do it all themselves. No casino does. They rely on third-party vendors for everything from payroll to surveillance software. And those vendors?” He paused for dramatic effect. “They’re the chink in the armor.”

He clicked a button on his tablet, and a flowchart appeared on the wall, showing a web of connections between the Diamond Casino and its external service providers.

What is Third-Party Vendor Risk?
Lester gestured at the chart. “When the casino hires outside companies, they’re adding more points of failure. These vendors might have weaker security than the Diamond itself, which means... they’re our way in.”

What They Use Vendors For:

“The Diamond relies on third parties for their payment systems, software updates, maintenance contracts, even janitorial services. Each one of these vendors has access to part of their operations.”
Why It’s a Problem:

“Every vendor adds a layer of risk. If the vendor gets breached, so does the casino. If the vendor slacks on security, the casino pays the price.”
Types of Third-Party Risks
Lester clicked again, bringing up a new slide. “Third-party risks aren’t just about IT breaches. They can hit the casino from all sides.”

Cybersecurity Risks:

“A vendor might get hacked, and their compromised systems could become a backdoor into the Diamond’s network.”
Compliance Risks:

“If the vendor doesn’t follow the rules—like GDPR or PCI DSS—the casino gets fined. Regulatory bodies don’t care whose fault it is.”
Operational Risks:

“Imagine if the company maintaining their surveillance cameras misses a routine check. One blind camera, and we’ve got our way in.”
Reputational Risks:

“If a vendor leaks customer data, the casino’s name is the one in the headlines.”
How the Casino Mitigates Vendor Risk
Lester’s smirk widened. “Of course, the Diamond isn’t clueless. They’ve got controls in place to manage these risks.”

Due Diligence:

“Before hiring a vendor, they vet them. Background checks, security audits, the whole nine yards.”
Contracts:

“Every vendor signs a contract that spells out exactly how they’re supposed to protect the casino’s data. Non-compliance? Huge penalties.”
Access Controls:

“Vendors only get access to what they absolutely need. A janitorial contractor isn’t getting anywhere near the vault.”
Monitoring:

“The casino keeps tabs on their vendors. Regular security checks, activity logs—you name it.”
Weak Links in Vendor Management
“But,” Lester said, leaning on his cane, “even the best vendor management has its cracks.”

Shared Credentials:

“Some vendors share login details among employees. If one person gets compromised, the whole system goes down.”
Outdated Software:

“Vendors might use old versions of the casino’s software—versions with known vulnerabilities. If we find one, we’re in.”
Lack of Oversight:

“The Diamond might miss a routine vendor audit, giving us an opening to exploit.”
Overlooked Vendors:

“Not every vendor gets the same scrutiny. A small cleaning company might get less attention than the IT contractor, even though they both have access.”
Our Opportunity
Lester stepped closer to the screen, his tone growing conspiratorial. “Here’s where we come in.”

Vendor-Specific Phishing:

“We target one of their vendors with a phishing email. If we compromise their account, we can pivot into the casino’s systems.”
Compromised Hardware:

“If a vendor supplies hardware—like security cameras or payment terminals—we swap it for tampered devices that give us remote access.”
Social Engineering:

“Vendors are even easier to manipulate than casino employees. Pretend to be an IT technician, and they’ll hand over credentials without thinking twice.”
Piggybacking on Vendor Access:

“If a vendor’s employees are onsite, we can follow them in, posing as part of their crew.”
The Diamond’s Blind Spot
Lester turned to face the crew, his expression deadly serious. “The Diamond Casino thinks they’ve covered all their bases, but their reliance on third-party vendors is a house of cards. All it takes is one weak link—a careless vendor, an unpatched system—and the whole thing comes crashing down.”

He smirked. “And when it does, we’ll be the ones walking away with the prize.”

The team exchanged glances, their confidence growing as Lester outlined the vulnerabilities. They knew that cracking the Diamond’s third-party defenses wouldn’t just be clever—it would be devastatingly effective.






 """)
    input("Press Enter To Return To The Menu")

def vocabulary9():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Third-Party Vendor Risk---"
        "Third-Party Vendor Risk": "The potential for vulnerabilities introduced by external service providers used by an organization.",
        "Cybersecurity Risks": "Risks involving the potential for third-party systems to be hacked and used as entry points.",
        "Compliance Risks": "The risk of regulatory violations due to a vendor's failure to follow legal requirements.",
        "Operational Risks": "Risks that occur when a vendor fails to deliver essential services, affecting the organization's operations.",
        "Reputational Risks": "Damage to an organization’s reputation caused by third-party failures, such as data breaches.",

        "---Vendor Risk Management Practices---"
        "Due Diligence": "The process of investigating and assessing a vendor's reliability and security before hiring them.",
        "Contracts": "Formal agreements that outline the vendor's responsibilities, including data protection and compliance.",
        "Access Controls": "Restricting vendors’ access to only the systems and data they need for their role.",
        "Monitoring": "Regularly tracking vendor activities and conducting security audits to ensure compliance.",

        "---Vendor Weak Points---"
        "Shared Credentials": "A security weakness where login details are shared among multiple vendor employees.",
        "Outdated Software": "Using older versions of software with known vulnerabilities that can be exploited.",
        "Lack of Oversight": "Failing to regularly audit or monitor a vendor’s security practices.",
        "Overlooked Vendors": "Vendors with less scrutiny, often due to their perceived lower importance, who may introduce risks.",

        "---Exploitation Methods---"
        "Vendor-Specific Phishing": "Targeting a vendor with phishing attacks to gain access to their systems.",
        "Compromised Hardware": "Supplying tampered hardware, such as security cameras or payment terminals, to gain remote access.",
        "Social Engineering": "Manipulating vendor employees into revealing sensitive information or providing unauthorized access.",
        "Piggybacking on Vendor Access": "Gaining unauthorized access by following a vendor’s employees into restricted areas.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu10():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section10()
        elif choice == "2":
            vocabulary10()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section10():
    print("\n-- Content Section --")
    type_out(""" Every move they make is dictated by rules, regulations, and policies designed to protect their business—and those rules create some of the toughest barriers we’ll face.”

He pointed at the diagram. “The casino doesn’t just run a business. It runs a fortress of legality, and if we don’t tread carefully, their compliance systems will bury us before we even get close to the vault.”

Governance and Compliance: What They Are
Lester gestured toward the first section of the diagram. “Let’s break this down. Governance and compliance aren’t just fancy terms—they’re the invisible security guards standing between us and a payday.”

Governance:

“This is how the casino runs its operations. Policies, procedures, frameworks—it’s the rules they live by to stay secure and profitable.”
Compliance:

“Compliance is all about following the law. If they break the rules, they get hit with fines, lawsuits, or worse. So, trust me, they’re not cutting corners here.”
Compliance Standards at the Diamond
Lester clicked to the next slide, displaying a list of regulations. “The Diamond operates under some serious oversight. These are the standards keeping them in line.”

PCI DSS (Payment Card Industry Data Security Standard):

“Any place that processes credit cards follows this one. It ensures payment data is encrypted, access is restricted, and systems are monitored. If we’re aiming at financial data, expect tight controls.”
GDPR (General Data Protection Regulation):

“The casino caters to international clients, so they’re bound by GDPR. This means customer data—names, emails, anything identifiable—is heavily protected.”
SOX (Sarbanes-Oxley Act):

“This one’s for financial transparency. They’ve got logs for everything—transactions, audits, even system access. If we touch anything, it’ll leave a trail.”
Local Gaming Regulations:

“The state has its own rules for casinos—background checks for employees, strict monitoring of financial activities, and real-time audits. Anything out of place gets flagged.”
Governance Frameworks
Lester adjusted his glasses, clicking to a flowchart of policies. “Now, governance is how they enforce all this. It’s their internal playbook for staying compliant.”

Risk Management Frameworks:

“We talked about risk management earlier. Governance frameworks like COBIT or ISO 31000 guide how they handle threats and protect their assets.”
Access Control Policies:

“They’ve got rules about who can access what. Employees need clearance for every action—vault access, system login, even clocking in and out.”
Incident Response Plans:

“If something goes wrong—like a breach—governance kicks in. They’ve got detailed playbooks to detect, contain, and recover.”
Data Retention Policies:

“Every piece of data—customer records, financial logs, surveillance footage—is kept or deleted based on strict rules. They don’t keep data longer than they’re legally allowed to.”
How Governance and Compliance Stop Us
Lester sighed, spinning around to face the team. “All these rules aren’t just there for show. They’re weapons designed to stop people like us.”

Audit Trails:

“Every action leaves a trace. If we tamper with the system or move funds, it’ll be logged—and that log will be reviewed.”
Continuous Monitoring:

“Real-time systems watch for anomalies. A single missed authentication, a failed login attempt, or a suspicious transaction? It’s flagged instantly.”
Legal Reporting Obligations:

“If we slip up, the casino has to report breaches to regulators. That means we’ll have law enforcement breathing down our necks before we’re out the door.”
Fines and Penalties:

“The casino is terrified of non-compliance because the penalties are astronomical. They’ve invested millions into making sure they’re airtight.”
Potential Weaknesses
Lester smirked, his voice dropping to a conspiratorial tone. “Of course, no system is perfect. Even governance and compliance have cracks.”

Human Oversight:

“Policies are only as good as the people enforcing them. An employee ignoring protocol is all the opening we need.”
Delayed Audits:

“Logs and audit trails are reviewed after the fact. If we move fast enough, we can slip out before anyone notices.”
Overreliance on Automation:

“They trust their systems to catch everything. But automation isn’t perfect—it can miss subtle deviations.”
Complexity:

“The more policies and frameworks they have, the harder it is to enforce them consistently. Complexity breeds mistakes.”
How We Exploit It
Lester leaned on his cane, his grin widening. “So, how do we turn their governance into our advantage? By finding the weak links and exploiting them.”

Policy Loopholes:

“Every policy has exceptions. If we find one—like an employee with outdated training—we can use it.”
Overwhelming Systems:

“Flood their monitoring systems with noise—failed logins, fake breaches, anything to distract them from our real moves.”
Forged Credentials:

“If their access policies rely on credentials, we forge them. A fake badge or stolen login could be our golden ticket.”
Delay Tactics:

“If we trigger a compliance mechanism, we make it seem minor—something they’ll deal with after we’re long gone.”
Lester’s Final Words
Lester turned to the team, his voice calm but commanding. “The Diamond Casino prides itself on its governance and compliance. But the truth is, the more rules they have, the more vulnerable they become. Rules create patterns—and patterns can be exploited. That’s exactly what we’re going to do.”

He tapped his cane against the floor, signaling the end of the briefing. “So, let’s get to work. If we can outthink their policies, the vault is as good as ours.”

The crew nodded, their determination renewed. As they left the room, Lester returned to his laptop, already poring over reports and regulations to uncover the cracks in the Diamond’s fortress of compliance. """)
    input("Press Enter To Return To The Menu")

def vocabulary10():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Governance and Compliance Basics---"
        "Governance": "The framework of rules, policies, and processes used to manage and secure an organization.",
        "Compliance": "The act of adhering to laws, regulations, standards, and ethical practices.",

        "---Compliance Standards---"
        "PCI DSS (Payment Card Industry Data Security Standard)": "A set of security standards for organizations that handle credit card transactions to ensure secure processing and storage.",
        "GDPR (General Data Protection Regulation)": "A regulation protecting the personal data and privacy of individuals within the European Union.",
        "SOX (Sarbanes-Oxley Act)": "A U.S. law requiring accurate financial reporting and robust internal controls.",
        "Local Gaming Regulations": "State or regional laws governing casino operations, including financial activities and employee background checks.",

        "---Governance Frameworks---"
        "Risk Management Frameworks": "Guidelines, such as COBIT or ISO 31000, that help organizations identify, assess, and manage risks.",
        "Access Control Policies": "Rules that dictate who can access specific systems, data, or resources within an organization.",
        "Incident Response Plans": "Predefined procedures for detecting, containing, and recovering from security incidents.",
        "Data Retention Policies": "Policies that determine how long specific types of data are stored or when they must be deleted.",

        "---Governance and Compliance Challenges---"
        "Audit Trails": "Logs that track every action taken within a system, used to detect unauthorized activities.",
        "Continuous Monitoring": "Real-time systems that monitor network activities for anomalies or threats.",
        "Legal Reporting Obligations": "Requirements to report security breaches or compliance failures to regulatory authorities.",
        "Fines and Penalties": "Monetary or legal repercussions for failing to comply with laws or regulations.",

        "---Weaknesses in Governance and Compliance---"
        "Human Oversight": "Errors or negligence by individuals responsible for enforcing governance and compliance.",
        "Delayed Audits": "The time lag between when actions are logged and when they are reviewed, creating potential blind spots.",
        "Overreliance on Automation": "Dependence on automated systems, which may fail to detect subtle threats.",
        "Complexity": "The difficulty of enforcing numerous rules and frameworks consistently, leading to mistakes or gaps.",

        "---Exploitation Methods---"
        "Policy Loopholes": "Exceptions or oversights within governance policies that can be exploited.",
        "Overwhelming Systems": "Flooding monitoring or compliance systems with distractions to conceal real threats.",
        "Forged Credentials": "Falsified access credentials used to bypass access control policies.",
        "Delay Tactics": "Causing minor compliance issues to divert attention from larger breaches.",
    }

    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu11():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section11()
        elif choice == "2":
            vocabulary11()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section11():
    print("\n-- Content Section --")
    type_out(""" Asset Management: Knowing Every Piece in Play
Lester tapped a key, and the map zoomed in on the casino's IT infrastructure. “Every cable, every server, every piece of tech in this place is cataloged, tracked, and monitored in real-time. Asset management isn't just about knowing what they have—it’s about ensuring nothing slips through the cracks.”

Inventory Management:

“The casino uses advanced inventory systems to log every device. Each server, terminal, and even point-of-sale machine is tagged with asset IDs. If something goes missing or unauthorized devices show up, alarms go off.”
Asset Baseline:

“They’ve got a baseline configuration for every critical system. That means they know exactly how each system should look—software, hardware, and even performance benchmarks. Deviate from that baseline, and their systems will know something’s up.”
Configuration Drift Detection:

“They monitor for ‘drift.’ If a server’s configuration changes, like unauthorized software or settings, it’s logged and flagged for investigation. No ‘accidental’ software installs are slipping through here.”
Critical Asset Identification:

“And let’s not forget: not all assets are created equal. The casino knows which servers handle financial transactions, which ones store customer data, and which ones run the slot machines. Those are locked down tighter than a politician’s alibi.”
Change Management: No Move Goes Unnoticed
Lester clicked to the next slide, showing a flowchart of the casino’s change management process. “Now, if we’re thinking about tampering with systems, we have another beast to deal with: change management. Every tweak, upgrade, and patch goes through an ironclad process.”

Change Requests:

“Any change—whether it’s updating software, adding new devices, or modifying access permissions—requires a formal request. No one can just ‘wing it.’”
Approval Workflow:

“Requests go through layers of approval. The casino’s IT admin, compliance team, and even external auditors might have to sign off, depending on the change.”
Testing Environments:

“Before changes go live, they’re tested in isolated environments. They’ll know if something breaks before it ever touches the main system.”
Post-Change Monitoring:

“Even after a change is implemented, it’s not over. They monitor the system for anomalies—performance dips, unauthorized access attempts, you name it.”
Auditing and Documentation:

“Every change is logged. Who requested it, why it was made, who approved it, and what the impact was. If we try to backdoor into a system and leave fingerprints, it’ll be all over their logs.”
How Asset and Change Management Work Together
Lester leaned forward, his voice dropping to a conspiratorial tone. “The real power here is how these systems work together. Asset management ensures they know every piece of hardware and software in play, while change management keeps a tight grip on anything that moves.”

Unauthorized Access Alerts:

“If we try to plug into a server or swap out a terminal, asset management will catch it. And if we try to mask it with a fake change request, the approval process will bury us.”
Real-Time Monitoring:

“These systems are interconnected. Any anomaly—a device that shouldn’t be there or a change that wasn’t approved—triggers alarms across the board.”
Incident Response Tied to Changes:

“The casino’s incident response team is primed to respond to unauthorized changes. If they see something they don’t like, they can roll back the system to a previous state in minutes.”
Lester’s Final Thoughts
Lester sighed, leaning back in his chair. “The Diamond doesn’t just protect its assets—it protects how those assets evolve. Every patch, every upgrade, every swap-out is tracked, reviewed, and locked down. To get what we want, we’d need to beat not just their systems but their processes, their people, and their paranoia.”

The crew sat in silence, digesting the daunting challenge ahead. For Lester, the complexity wasn’t discouraging—it was invigorating. A smirk played across his lips as he rolled back to his laptop. “Alright,” he said softly, “let’s see how bulletproof they really are.”

 """)
    input("Press Enter To Return To The Menu")

def vocabulary11():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Asset Management Terms---"
        "Asset Management": "The process of identifying, tracking, and managing all physical and digital assets within an organization.",
        "Inventory Management": "The practice of cataloging and monitoring all devices, software, and systems in use.",
        "Asset Baseline": "A predefined configuration for assets that serves as a reference point for normal behavior.",
        "Configuration Drift Detection": "The monitoring of systems for unauthorized or unintended changes in configuration.",
        "Critical Asset Identification": "The process of determining which assets are most essential to an organization’s operations and security.",

        "---Change Management Terms---"
        "Change Management": "The structured process for making changes to systems, software, or configurations within an organization.",
        "Change Requests": "Formal proposals for modifications to a system, including the reason and details of the change.",
        "Approval Workflow": "A multi-step process requiring permission from stakeholders before a change is implemented.",
        "Testing Environments": "Isolated systems used to test changes before they are applied to the live environment.",
        "Post-Change Monitoring": "The observation of systems after a change to detect issues or anomalies.",
        "Auditing and Documentation": "The practice of recording all changes, including who approved and implemented them, for future review.",

        "---Combined Functions---"
        "Unauthorized Access Alerts": "Notifications triggered by attempts to access or modify assets without proper authorization.",
        "Real-Time Monitoring": "The continuous observation of systems to detect and respond to unauthorized changes or anomalies.",
        "Incident Response Tied to Changes": "The integration of change monitoring with incident response plans to address issues caused by unauthorized modifications.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu12():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section12()
        elif choice == "2":
            vocabulary12()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section12():
    print("\n-- Content Section --")
    type_out(""" Audits and assessments. These are the tools they use to find weaknesses before people like us do. It’s their way of staying one step ahead. But... if we play this right, these tools could also work in our favor.”

What Are Audits and Assessments?
Lester highlighted a simplified diagram of the casino’s security workflow. “The casino doesn’t just assume its defenses are solid—they test them. Constantly.”

Audits:

“These are formal reviews. They go through their systems, processes, and policies with a fine-tooth comb, looking for anything that’s out of place. It’s like a report card for their security.”
Assessments:

“These are broader evaluations. They measure risks, identify vulnerabilities, and test controls. Think of them as mock drills to prepare for real threats.”
Types of Audits
Lester flipped to a slide showing different types of audits. “Let’s break down what they’re looking at and why it matters to us.”

Internal Audits:

“These are done by the casino’s own staff. They check everything—system logs, employee compliance, financial records. It’s their way of catching problems before outsiders do.”
External Audits:

“Third-party firms come in for these. They’re hired to make sure the casino meets industry standards and regulations, like PCI DSS or local gaming laws. These guys don’t play favorites.”
Financial Audits:

“Every penny in and out of this place is tracked. If we try to move money through their systems, you can bet it’ll get flagged during the next financial audit.”
Compliance Audits:

“These ensure the casino is following all the rules—GDPR, SOX, you name it. Any deviation from the playbook? Big trouble.”
Types of Assessments
Lester switched to a new slide, this one focusing on assessments. “Now, let’s talk about how they stress-test their systems.”

Vulnerability Assessments:

“These look for weak points in their network, like unpatched software or misconfigured firewalls. Anything we could exploit.”
Penetration Tests (Pen Tests):

“Ethical hackers try to break in—physically and digitally. If they succeed, the casino fixes the holes. If they don’t, well, they fix what almost worked.”
Risk Assessments:

“These measure the likelihood and impact of different threats. They prioritize what to fix first based on the damage it could cause.”
Red Team Exercises:

“The hardcore stuff. A specialized team simulates a full-blown attack. They use all the tricks in the book—phishing, physical breaches, malware—you name it.”
How Audits and Assessments Stop Us
Lester sighed and leaned against the table. “Now, here’s why all this is bad news for us.”

Identifying Weaknesses:

“Every time they find a gap, they patch it. That means fewer entry points for us.”
Incident Preparedness:

“If something goes wrong, their assessments have already prepped them to respond. They’ve run the scenarios—they know what to do.”
Real-Time Monitoring Improvements:

“Assessments often lead to better monitoring tools. That SIEM system we hate? It’s probably there because of a red team report.”
Accountability:

“Audits ensure someone’s always responsible. If an employee screws up, it’ll get flagged and fixed fast.”
Potential Weaknesses
But Lester wasn’t done. He straightened up and smirked. “Of course, these audits and assessments aren’t perfect. They’re run by humans, and humans make mistakes.”

Audit Fatigue:

“When you audit everything, all the time, people start cutting corners. That’s where errors creep in.”
Overconfidence:

“A perfect audit score can make them complacent. They might ignore minor issues that we could exploit.”
Delayed Implementation:

“Just because they find a problem doesn’t mean it gets fixed right away. Bureaucracy slows everything down.”
Focus on High-Priority Risks:

“They’ll focus on the big stuff and sometimes overlook smaller vulnerabilities. A weak employee password? Probably not at the top of their list.”
How We Exploit It
Lester tapped his cane on the floor, drawing the crew’s attention. “If we’re smart, we can turn their strengths into weaknesses.”

Leverage Audit Findings:

“If we get our hands on an internal audit report, it’ll tell us exactly where they’re vulnerable.”
Simulate a False Alarm:

“Trigger a small incident, like a failed login or a fake phishing attempt. While they’re focused on investigating that, we make our real move.”
Exploit Bureaucracy:

“Even if they know a system needs patching, it could take weeks to get approval. We strike before they close the gap.”
Target Low-Priority Areas:

“We aim for the things they’re not worried about—like that neglected server running an old application.”
Lester’s Closing Words
Lester turned back to his laptop, the corners of his mouth curling into a grin. “The Diamond Casino thinks audits and assessments make them invincible. But all they really do is create a map of their strengths and weaknesses—a map we’re going to steal and use against them. Let’s get to work.”

The crew exchanged knowing looks, their confidence building with every detail Lester uncovered. The heist wasn’t just about brute force anymore—it was becoming a game of intellect, precision, and exploiting overconfidence.

 """)
    input("Press Enter To Return To The Menu")

def vocabulary12():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Audit Types---"
        "Audits": "Formal reviews of systems, processes, and policies to identify vulnerabilities or ensure compliance.",
        "Internal Audits": "Audits conducted by the organization’s own staff to identify and address issues before external reviews.",
        "External Audits": "Audits performed by third-party firms to ensure compliance with industry standards and regulations.",
        "Financial Audits": "Audits that focus on tracking financial records and ensuring proper accounting practices.",
        "Compliance Audits": "Audits that verify an organization is adhering to laws, regulations, and industry standards.",

        "---Assessment Types---"
        "Assessments": "Broad evaluations that measure risks, identify vulnerabilities, and test controls.",
        "Vulnerability Assessments": "Evaluations that identify weak points in systems, such as unpatched software or misconfigurations.",
        "Penetration Tests (Pen Tests)": "Simulated attacks by ethical hackers to identify and exploit vulnerabilities.",
        "Risk Assessments": "Evaluations that measure the likelihood and impact of threats to prioritize mitigation efforts.",
        "Red Team Exercises": "Simulations of full-scale attacks by a specialized team to test an organization’s defenses.",

        "---Benefits and Challenges of Audits and Assessments---"
        "Identifying Weaknesses": "Audits and assessments uncover vulnerabilities and gaps in an organization’s defenses.",
        "Incident Preparedness": "Prepares an organization to respond effectively to real-world incidents.",
        "Real-Time Monitoring Improvements": "Enhances monitoring systems based on findings from assessments.",
        "Audit Fatigue": "The tendency for employees to become complacent or cut corners when audits are frequent.",
        "Overconfidence": "A false sense of security from positive audit results, leading to complacency.",
        "Delayed Implementation": "The lag between identifying vulnerabilities and implementing fixes.",
        "Focus on High-Priority Risks": "Prioritizing major threats while potentially overlooking smaller vulnerabilities.",

        "---Exploitation Strategies---"
        "Leverage Audit Findings": "Using audit results to identify and exploit known vulnerabilities.",
        "Simulate a False Alarm": "Triggering a minor incident to distract security teams while conducting the real attack.",
        "Exploit Bureaucracy": "Taking advantage of delays in patching or fixing vulnerabilities due to organizational processes.",
        "Target Low-Priority Areas": "Focusing on neglected or less-protected systems that may still provide valuable access.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu13():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section13()
        elif choice == "2":
            vocabulary13()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section13():
    print("\n-- Content Section --")
    type_out(""" What is Cyber Resilience?
Lester tapped a key, zooming in on the chart. “Cyber resilience is their ability to keep running, no matter what we throw at them. Even if we knock out a piece of their system, they’ll recover before we can finish the job.”

Disaster Recovery:

“If their systems go down—whether it’s from a cyberattack, power outage, or hardware failure—they’ve got a plan to get back online fast.”
Business Continuity:

“This is the bigger picture. Even if their main systems are toast, they’ve got backups and manual processes to keep the casino running. Slot machines, card tables, customer services—they’ll keep going.”
Incident Response:

“They’ve trained for this. The second they spot something wrong, they’ll isolate the problem, minimize damage, and start recovery. Think of it like sealing off a leaking submarine compartment.”
Redundancy: Their Secret Weapon
Lester switched to a new slide, this one showing a mirrored data center. “Now, redundancy is how they ensure resilience. Every critical system has a backup—and sometimes, a backup for the backup.”

Server Redundancy:

“They use mirrored servers in different locations. If one server crashes or gets compromised, the other takes over instantly.”
Data Redundancy:

“Their customer and transaction data are stored in multiple places—locally and offsite. Even if we delete something, they’ll have a copy somewhere.”
Network Redundancy:

“If one network path fails, their systems automatically reroute traffic through another path. No downtime, no disruptions.”
Power Redundancy:

“Generators, UPS systems, solar backups—you name it. If the grid fails, they’ll keep running without breaking a sweat.”
Their Strategy Against Us
Lester leaned against the table, the corners of his mouth twitching into a grin. “So, what does this mean for us? It means even if we pull off a perfect breach, the Diamond will fight back.”

Failover Systems:

“If we knock out their primary servers, their failover systems will take over in seconds. We won’t have time to exploit the downtime.”
Immutable Backups:

“They’ve probably got immutable backups—copies that can’t be deleted or tampered with. Ransomware? Useless.”
Isolated Networks:

“They’ll isolate compromised systems to stop malware from spreading. Forget taking down the whole network.”
Incident Response Teams:

“And let’s not forget their response teams. They’ve run drills for this exact situation. The moment we trip an alarm, they’ll be on us.”
Potential Weak Points
But Lester wasn’t done. He straightened up and tapped his cane against the floor. “Of course, even the best systems have flaws. Here’s where we might find some cracks.”

Complexity:

“The more redundancy they have, the more complex their systems are. And complexity breeds mistakes.”
Human Error:

“Redundant systems still need people to manage them. One careless admin forgetting a step? That’s our way in.”
Lag in Failover Systems:

“Even the fastest failover systems have a delay—sometimes a few seconds, sometimes minutes. That’s all the time we need.”
Overconfidence in Resilience:

“If they think their systems are bulletproof, they might not monitor them as closely. Overconfidence is as good as a weakness.”
How We Exploit It
Lester’s smirk widened as he outlined the team’s potential strategy. “Here’s how we turn resilience into an advantage.”

Simultaneous Attacks:

“Hit multiple systems at once. Redundancy works best when one thing goes wrong, not everything.”
Target Recovery Systems:

“Instead of attacking the primary systems, go for the backups. Take those out, and they’ve got nowhere to failover.”
Exploit Failover Lag:

“Create chaos during the handoff between primary and backup systems. That’s when they’re most vulnerable.”
Leverage Overconfidence:

“If they think they’ve got us beat, they’ll focus on recovery instead of looking for a second attack.”
Lester’s Final Thoughts
Lester turned back to the screen, his grin fading into a look of quiet determination. “The Diamond Casino didn’t become one of the most secure places in the city by accident. They’ve invested millions into making sure they can take a hit and keep standing. But no system is perfect. If we can find the weak link in their resilience, we’ll make this heist one for the books.”

The crew nodded, the weight of the challenge hanging in the air. For Lester, the challenge wasn’t discouraging—it was exhilarating. The more the casino fought back, the sweeter the victory would be. """)
    input("Press Enter To Return To The Menu")

def vocabulary13():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Cyber Resilience Terms---"
        "Cyber Resilience": "The ability of an organization to continue operating effectively despite cyberattacks, failures, or disruptions.",
        "Disaster Recovery": "A set of procedures and tools used to restore operations quickly after a system failure or attack.",
        "Business Continuity": "The ability to maintain essential functions during and after a disaster or disruption.",
        "Incident Response": "A structured approach to detecting, responding to, and recovering from security incidents.",

        "---Redundancy Types---"
        "Redundancy": "The duplication of critical systems or components to ensure availability in case of failure.",
        "Server Redundancy": "Using mirrored servers to ensure continuity if one server fails.",
        "Data Redundancy": "Storing data in multiple locations to protect against data loss or corruption.",
        "Network Redundancy": "Using alternate network paths to ensure connectivity in case of a failure.",
        "Power Redundancy": "Using backup power systems like generators and UPS to maintain operations during outages.",

        "---Resilience Strategies---"
        "Failover Systems": "Backup systems that automatically take over when the primary system fails.",
        "Immutable Backups": "Data backups that cannot be altered or deleted, protecting against ransomware and tampering.",
        "Isolated Networks": "Segments of a network that are separated to prevent the spread of malware or attacks.",
        "Incident Response Teams": "Specialized groups tasked with managing and mitigating security incidents.",

        "---Weaknesses and Exploits---"
        "Complexity": "The increased likelihood of errors in systems due to their intricate design and redundant components.",
        "Human Error": "Mistakes made by administrators or operators that can compromise resilience systems.",
        "Lag in Failover Systems": "The delay between a system failure and the activation of its backup, creating a temporary vulnerability.",
        "Overconfidence in Resilience": "An organization’s belief that its systems are invulnerable, leading to complacency in monitoring or defense.",
    }

    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu14():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section14()
        elif choice == "2":
            vocabulary14()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section14():
    print("\n-- Content Section --")
    type_out("""  The casino’s security architecture isn’t just about tech or policies—it’s about how all those pieces fit together. It’s the big picture. And if we’re going to pull this off, we need to know how their entire operation is wired.”

He gestured to the diagram. “Think of this as their blueprint for keeping people like us out. Let’s break it down.”

What is Security Architecture?
Lester leaned on his cane and pointed to the screen. “Security architecture is how they design and implement their defenses. It’s not just about individual controls—it’s about how everything works together to protect their assets.”

Defense in Depth:

“This is their core strategy. They don’t rely on just one layer of defense. It’s like an onion—each layer protects the one beneath it.”
Zones of Control:

“The casino is divided into zones—public areas, restricted staff zones, and critical infrastructure. Each zone has its own security requirements.”
Security Frameworks:

“They follow frameworks like NIST or ISO 27001 to build their architecture. These frameworks are all about best practices—ensuring no gaps in coverage.”
Integrated Systems:

“Every system—cameras, access controls, network firewalls—is connected. If one system detects a threat, the others react automatically.”
Key Components of Security Architecture
Lester tapped a key, zooming in on the diagram. “Now, let’s look at the specific pieces in play.”

Perimeter Security:

“The outermost layer. This is where firewalls and intrusion prevention systems (IPS) stop threats before they even get in.”
Endpoint Security:

“Each device—computers, cameras, slot machines—has its own protections, like antivirus and application controls.”
Network Segmentation:

“They’ve divided their network into segments. That means even if we get into one part, we won’t automatically have access to the rest.”
Access Management:

“Strict controls on who can go where. Multi-factor authentication, biometric scanners, and role-based access control keep everyone in their lane.”
Data Protection:

“Encryption, data masking, and backup systems ensure that even if we steal something, it won’t be usable.”
Advanced Security Measures
The crew groaned as Lester switched to yet another slide, this one showing more sophisticated systems.

Zero Trust Architecture:

“They don’t trust anyone by default—not employees, not systems. Every request for access has to be verified.”
SIEM (Security Information and Event Management):

“This is their brain. It collects data from all their systems and analyzes it for threats in real-time.”
Threat Intelligence Integration:

“They’ve got feeds that update them on the latest threats. If someone attacks a casino across town, the Diamond will know about it in minutes.”
Incident Response Automation:

“If something goes wrong, automated systems will isolate the threat and notify their security team instantly.”
Challenges for Us
Lester sighed, pacing in front of the screen. “Now, here’s why this makes our job harder.”

Redundant Systems:

“Even if we take down one piece, the others will keep running. Firewalls, backup servers, alternate network paths—it’s all designed to keep us out.”
Visibility:

“Their SIEM gives them a bird’s-eye view of everything happening in real-time. One slip, and we’re caught.”
Adaptive Security:

“They’ve got systems that learn. If we try the same trick twice, they’ll catch on.”
Restricted Movement:

“Even if we get into one zone, we’ll hit a wall trying to move to another. Each segment is locked tighter than the last.”
Potential Weak Points
Lester smirked, leaning on the table. “Of course, no architecture is perfect. Let’s talk about where we might find cracks.”

Misconfigured Systems:

“A firewall with the wrong rules, an endpoint missing updates—these are the weak links we’ll exploit.”
Overreliance on Automation:

“Automated systems can only respond to what they know. A novel attack might slip through.”
Integration Gaps:

“When you connect so many systems, something’s bound to fall through the cracks—data that isn’t shared, alerts that don’t trigger.”
Human Error:

“At the end of the day, people run these systems. And people make mistakes.”
How We Exploit It
Lester’s grin widened as he addressed the crew. “Here’s how we turn their fortress into a playground.”

Test for Misconfigurations:

“Scan for systems that aren’t set up properly—firewalls with open ports, forgotten access permissions.”
Target Integration Points:

“Focus on where their systems connect. A gap in integration could give us a backdoor.”
Distract the SIEM:

“Flood their systems with false alarms. If the SIEM is chasing ghosts, it won’t see us coming.”
Leverage Human Error:

“Social engineering, phishing—if we can trick a person into making a mistake, we bypass all the tech.”
Lester’s Closing Words
Lester turned back to the diagram, tapping his cane against the floor for emphasis. “The Diamond Casino built its security architecture to be impenetrable. But the more complicated a system gets, the more vulnerable it becomes. If we can find the cracks—and we will—we’ll make history.”

The crew exchanged determined glances, the weight of the task settling over them. For Lester, it wasn’t just about pulling off the impossible—it was about proving that even the most sophisticated security could be outsmarted.

  """)
    input("Press Enter To Return To The Menu")

def vocabulary14():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Security Architecture Basics---"
        "Security Architecture": "The design and implementation of security controls and systems to protect an organization's assets.",
        "Defense in Depth": "A security strategy that uses multiple layers of protection to safeguard systems and data.",
        "Zones of Control": "Dividing an organization into security zones, each with its own requirements and access controls.",
        "Security Frameworks": "Guidelines like NIST or ISO 27001 that outline best practices for building and maintaining security systems.",
        "Integrated Systems": "Interconnected security systems that share information and respond to threats collectively.",

        "---Key Components---"
        "Perimeter Security": "The outermost layer of protection, including firewalls and intrusion prevention systems.",
        "Endpoint Security": "Protections for individual devices, such as antivirus software and application controls.",
        "Network Segmentation": "Dividing a network into isolated segments to limit the spread of threats.",
        "Access Management": "Systems and policies that regulate who can access specific resources or zones.",
        "Data Protection": "Methods like encryption and data masking to ensure sensitive data remains secure.",

        "---Advanced Security Measures---"
        "Zero Trust Architecture": "A security model where no user or system is trusted by default, requiring verification for every access request.",
        "SIEM (Security Information and Event Management)": "A system that collects and analyzes data from across the network to detect and respond to threats.",
        "Threat Intelligence Integration": "Using external and internal sources to stay informed about the latest threats.",
        "Incident Response Automation": "Automated tools and processes that detect, isolate, and respond to security incidents.",

        "---Challenges for Security Architecture---"
        "Redundant Systems": "Backup systems that ensure continuity if one component fails.",
        "Visibility": "The ability of security tools to monitor and detect activities across all systems.",
        "Adaptive Security": "Systems that adjust to evolving threats by learning from past incidents.",
        "Restricted Movement": "Controls that limit lateral movement within a network or between security zones.",

        "---Weak Points---"
        "Misconfigured Systems": "Systems that have incorrect settings, leaving them vulnerable to attacks.",
        "Overreliance on Automation": "Dependence on automated systems that may fail to detect novel or subtle threats.",
        "Integration Gaps": "Weaknesses in how interconnected systems share data and alerts.",
        "Human Error": "Mistakes made by administrators or users that compromise security.",

        "---Exploitation Strategies---"
        "Test for Misconfigurations": "Identifying and exploiting improperly set up systems like firewalls or access controls.",
        "Target Integration Points": "Focusing on vulnerabilities in the connections between different systems.",
        "Distract the SIEM": "Flooding monitoring systems with false alarms to conceal real attacks.",
        "Leverage Human Error": "Using techniques like phishing to trick individuals into making mistakes that compromise security.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################
def submenu15():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section15()
        elif choice == "2":
            vocabulary15()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def content_section15():
    print("\n-- Content Section --")
    type_out(""" What is Security Infrastructure?
Lester gestured at the diagram. “Think of this as the foundation of everything we’ve talked about so far. Security infrastructure is the physical and digital backbone that supports their defenses.”

Physical Infrastructure:

“This is the tangible stuff—firewalls, servers, network cables. Anything you can touch or plug in.”
Logical Infrastructure:

“This is the software side—firewall rules, VPN configurations, user access permissions. The invisible glue holding everything together.”
Hybrid Infrastructure:

“Most of their systems are hybrid—physical devices with software overlays. For example, their surveillance cameras aren’t just cameras; they’re IoT devices with built-in analytics.”
Core Components of the Diamond’s Security Infrastructure
Lester clicked to the next slide, showing a breakdown of the casino’s core systems. “Let’s take a closer look at what we’re dealing with.”

Firewalls:

“These are their first line of defense. Hardware firewalls filter traffic coming into their network, while software firewalls handle the internal traffic.”
Intrusion Detection and Prevention Systems (IDPS):

“IDPS monitors traffic for suspicious behavior. If it spots something off, it either logs it (detection) or shuts it down (prevention).”
Virtual Private Network (VPN):

“Employees working remotely or contractors accessing the system? They’re going through a VPN. Encrypted tunnels make sure their traffic stays private.”
Network Access Control (NAC):

“NAC ensures only authorized devices can connect to their network. Anything unfamiliar gets quarantined.”
IoT Devices:

“Surveillance cameras, slot machines, even thermostats. These aren’t just devices—they’re endpoints on the network, each with its own vulnerabilities.”
Advanced Systems in Place
The crew groaned as Lester moved to another slide, this one more technical. “The Diamond didn’t stop at the basics. They’ve gone high-tech.”

Cloud Infrastructure:

“Some of their critical systems, like customer data and backups, are stored in the cloud. It’s scalable and redundant, but it adds another layer of security to deal with.”
Endpoint Detection and Response (EDR):

“This monitors every device for threats. If someone tries to tamper with a terminal, EDR catches it.”
DDoS Protection:

“Their web-facing systems, like reservation portals, are protected by services that block Distributed Denial of Service attacks.”
Secure Gateways:

“Any data leaving their network goes through a secure web gateway to prevent leaks or malware downloads.”
Software-Defined Networking (SDN):

“Their network adapts in real-time. If an attack happens, SDN can reroute traffic or isolate segments to contain the damage.”
How Infrastructure Stops Us
Lester paced as he explained, the crew furrowing their brows. “Here’s why their infrastructure makes our job a nightmare.”

Real-Time Monitoring:

“IDPS and EDR work in tandem to spot and shut down threats in seconds.”
Encryption Everywhere:

“From the VPN to their cloud storage, everything is encrypted. Even if we intercept something, it’ll be useless without the keys.”
Device Quarantines:

“If we try to plug in an unauthorized device, NAC will isolate it instantly.”
Adaptive Systems:

“Their SDN and cloud infrastructure adapt to attacks. Taking down one part won’t cripple the whole network.”
Potential Weak Points
Lester smirked, leaning on the table. “Of course, no infrastructure is flawless. Even the Diamond’s tech has cracks.”

Legacy Systems:

“Not everything is cutting-edge. If they’re running old software or hardware in some areas, that’s a weakness we can exploit.”
IoT Vulnerabilities:

“IoT devices like cameras and thermostats are notoriously insecure. A single unpatched camera could be our way in.”
Overconfigured Firewalls:

“Too many rules can create blind spots. If they’ve overcomplicated their firewall settings, we might find a gap.”
Cloud Misconfigurations:

“The cloud is great for them, but if it’s not configured properly, it’s great for us too.”
How We Exploit It
Lester’s grin widened as he addressed the crew. “Here’s how we can turn their fortress into swiss cheese.”

Scan for IoT Gaps:

“Target devices like cameras or slot machines. If one’s vulnerable, it could give us a foothold.”
Look for Legacy Systems:

“Find the oldest part of their infrastructure—the stuff that hasn’t been updated in years. That’s where the cracks are.”
Test Firewall Rules:

“Probe their firewalls for gaps. If they’ve got too many rules, something might slip through.”
Exploit Cloud Misconfigurations:

“If we can find a misconfigured storage bucket or admin panel, it could be a goldmine.”
Lester’s Final Words
Lester turned to face the crew, his expression a mix of determination and exhilaration. “The Diamond Casino didn’t build this infrastructure to stop average criminals—they built it to stop the best. But the more systems they have, the more points of failure we can exploit. If we’re smart, if we’re precise, we’ll tear through their defenses like paper.”

The crew nodded, their confidence growing despite the daunting challenge. Lester tapped his cane against the floor, signaling the end of the briefing. “Let’s make them regret spending all that money.”

  """)
    input("Press Enter To Return To The Menu")

def vocabulary15():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Security Infrastructure Basics---"
        "Security Infrastructure": "The hardware, software, and network components that form the backbone of an organization's defenses.",
        "Physical Infrastructure": "Tangible components like firewalls, servers, and network cables.",
        "Logical Infrastructure": "Software-based controls like firewall rules, access permissions, and VPN configurations.",
        "Hybrid Infrastructure": "A combination of physical devices and software systems working together, like IoT-enabled cameras.",

        "---Core Components---"
        "Firewalls": "Systems that filter incoming and outgoing network traffic based on predefined rules.",
        "Intrusion Detection and Prevention Systems (IDPS)": "Systems that monitor network traffic for suspicious activity and take action to block or log it.",
        "Virtual Private Network (VPN)": "Encrypted tunnels that ensure private and secure communication over a public network.",
        "Network Access Control (NAC)": "Systems that restrict network access to authorized devices only.",
        "IoT Devices": "Internet-connected devices like cameras, slot machines, or thermostats that interact with the network.",

        "---Advanced Systems---"
        "Cloud Infrastructure": "Offsite data storage and services used for scalability and redundancy.",
        "Endpoint Detection and Response (EDR)": "Solutions that monitor endpoints for threats and provide real-time response capabilities.",
        "DDoS Protection": "Tools and services that block Distributed Denial of Service attacks aimed at overwhelming systems.",
        "Secure Gateways": "Systems that filter data leaving the network to prevent leaks or malware.",
        "Software-Defined Networking (SDN)": "Networks that can adapt dynamically to threats by rerouting traffic or isolating segments.",

        "---Challenges for Security Infrastructure---"
        "Real-Time Monitoring": "Continuous observation of network and system activity to detect and respond to threats.",
        "Encryption Everywhere": "The practice of encrypting all data, whether at rest or in transit, to ensure confidentiality.",
        "Device Quarantines": "Processes that isolate unauthorized or compromised devices to prevent network access.",
        "Adaptive Systems": "Infrastructure that dynamically adjusts to threats and failures to maintain functionality.",

        "---Weak Points---"
        "Legacy Systems": "Older hardware or software that may have unpatched vulnerabilities.",
        "IoT Vulnerabilities": "Security flaws in internet-connected devices that can serve as entry points for attackers.",
        "Overconfigured Firewalls": "Complex firewall rules that may create gaps or blind spots in security.",
        "Cloud Misconfigurations": "Improperly set up cloud environments that expose sensitive data or administrative controls.",

        "---Exploitation Strategies---"
        "Scan for IoT Gaps": "Identifying and targeting vulnerabilities in internet-connected devices like cameras or sensors.",
        "Look for Legacy Systems": "Finding outdated systems that are more likely to have exploitable weaknesses.",
        "Test Firewall Rules": "Probing for gaps or errors in firewall configurations to bypass network defenses.",
        "Exploit Cloud Misconfigurations": "Leveraging improperly secured cloud resources to gain access to data or systems.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################

def submenu16():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section16()
        elif choice == "2":
            vocabulary16()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section16():
    print("\n-- Content Section --")
    type_out(""" The crew leaned in closer as Lester pulled up the next set of files, this time showcasing a grid of users, devices, and permissions labeled “IAM.” The Diamond Casino’s Identity and Access Management (IAM) system wasn’t just a part of its security—it was the gatekeeper to everything.

“Alright, listen up,” Lester began, pointing to the diagram. “IAM is the backbone of the casino’s access controls. If anyone gets near their critical systems, vaults, or data, it’s because IAM lets them. And trust me, this system doesn’t just hand out keys—it verifies, checks, and double-checks every move.”

What is IAM?
Lester clicked on the first slide. “IAM is how the casino controls who gets in, what they can access, and what they can do. Every employee, contractor, and system is tied into it.”

Identification:

“This is the first step. It answers the question: who are you? Every user and device has a unique ID.”
Authentication:

“Prove it. Whether it’s a password, a biometric scan, or a token, the system needs evidence that you are who you claim to be.”
Authorization:

“Now that we know who you are, what can you do? This step checks your permissions.”
Accounting:

“Every action gets logged. Who accessed what, when, and how—it’s all recorded for audits.”
IAM Solutions at the Diamond
Lester zoomed into the casino’s IAM diagram, outlining the specific tools they likely use.

Multi-Factor Authentication (MFA):

“No single passwords here. Employees need at least two methods to log in—like a fingerprint and a one-time code.”
Role-Based Access Control (RBAC):

“Access is tied to job roles. A janitor can’t see financial records, and a pit boss can’t touch IT systems.”
Privileged Access Management (PAM):

“Admin accounts are locked down. Even IT staff need special approval to make critical changes.”
Single Sign-On (SSO):

“One set of credentials gets employees into multiple systems—but it’s all tied to IAM, so if something feels off, they shut it all down.”
IAM Challenges for Us
Lester sighed as he brought up the next slide, showing the difficulties IAM posed for their heist.

Strict Authentication:

“Passwords aren’t enough. Biometric locks, hardware tokens—they’ve got layers of authentication.”
Granular Permissions:

“Even if we steal a valid user’s credentials, their permissions might not get us anywhere useful.”
Behavioral Analysis:

“IAM tracks patterns. If someone logs in at an unusual time or location, alarms go off.”
Session Monitoring:

“It doesn’t stop after you log in. Every action is monitored. Too many unusual commands? Game over.”
Weaknesses in IAM
But Lester wasn’t one to give up easily. He grinned as he highlighted the cracks in even the most robust IAM systems.

Shared Credentials:

“Sometimes employees share accounts to save time. It’s a big no-no, but it happens.”
Phishing Targets:

“The weakest part of IAM isn’t the tech—it’s the people. A well-crafted phishing email can get us access without a fight.”
Lack of Real-Time Updates:

“Some systems don’t update permissions immediately. If we act fast, we might exploit old access levels.”
Forgotten Privileges:

“Inactive accounts or old permissions can linger if they’re not cleaned up. A dormant account might be our golden ticket.”
How We Exploit It
Lester’s tone turned conspiratorial as he addressed the team. “Here’s how we turn their IAM fortress into a revolving door.”

Social Engineering:

“Convince an employee to share their login. Pretend to be IT, send a fake update notice—whatever works.”
Target Shared Accounts:

“If employees share credentials, we don’t just get one user—we get everyone tied to that account.”
Phish for MFA Bypass:

“Fake emails with a malicious login portal can capture passwords and trick users into giving us their MFA codes.”
Exploit Dormant Accounts:

“Find an account that hasn’t been used in months but still has access. These often slip through the cracks.”
Lester’s Final Thoughts
Lester turned to face the crew, his expression serious but eager. “IAM is their strongest line of defense, but it’s also their most human system. Every piece of tech in it is only as good as the people managing it—and people, my friends, are predictable. We find the gaps, we exploit the trust, and we turn their IAM into our ticket to the vault.”

  """)
    input("Press Enter To Return To The Menu")

def vocabulary16():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---IAM Basics---"
        "Identity and Access Management (IAM)": "A framework of policies and technologies that ensures the right individuals access the right resources at the right times.",
        "Identification": "The process of identifying a user, system, or device by assigning a unique identifier.",
        "Authentication": "Verifying the identity of a user, typically using credentials like passwords, biometrics, or tokens.",
        "Authorization": "Determining what resources or actions a user is permitted to access or perform.",
        "Accounting": "Logging and tracking user activities within a system for monitoring and auditing purposes.",

        "---IAM Solutions---"
        "Multi-Factor Authentication (MFA)": "A security system requiring two or more forms of authentication to verify a user's identity.",
        "Role-Based Access Control (RBAC)": "A method of restricting access based on a user's role within an organization.",
        "Privileged Access Management (PAM)": "Tools and policies designed to secure and manage privileged accounts with elevated access.",
        "Single Sign-On (SSO)": "An authentication method allowing a user to log in once and access multiple systems without re-authenticating.",

        "---Challenges in IAM---"
        "Strict Authentication": "The use of multiple layers of identity verification to ensure only authorized users gain access.",
        "Granular Permissions": "Fine-tuned control over which resources a user or role can access and the actions they can perform.",
        "Behavioral Analysis": "Monitoring user behavior to detect anomalies, such as unusual login times or locations.",
        "Session Monitoring": "Tracking user activities during a session to identify suspicious behavior.",

        "---Weak Points---"
        "Shared Credentials": "The practice of multiple users sharing one set of credentials, weakening accountability and security.",
        "Phishing Targets": "Users who are tricked into revealing their credentials through fraudulent communications.",
        "Lack of Real-Time Updates": "Delays in updating permissions, leaving systems vulnerable to exploits.",
        "Forgotten Privileges": "Dormant or inactive accounts that retain access and can be exploited.",

        "---Exploitation Strategies---"
        "Social Engineering": "Manipulating individuals into divulging confidential information or granting access.",
        "Target Shared Accounts": "Exploiting accounts used by multiple people to gain broader access.",
        "Phish for MFA Bypass": "Tricking users into revealing both their password and multi-factor authentication code.",
        "Exploit Dormant Accounts": "Using inactive accounts with retained access to bypass security controls.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################
    
def submenu17():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section17()
        elif choice == "2":
            vocabulary17()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section17():
    print("\n-- Content Section --")
    type_out(""" “Alright, team,” he began. “We’ve talked about how the Diamond keeps itself secure. But no system is perfect, and every fortress has cracks. Those cracks? They’re called vulnerabilities. And when you know how to exploit them, they’re your ticket in.”

He clicked to a new slide. “Now, vulnerabilities don’t mean squat unless someone knows how to use them. That’s where attacks come in. Let me show you how the casino’s defenses can be turned against them.”

What Are Vulnerabilities and Attacks?
Lester highlighted the first section of his diagram. “A vulnerability is any weakness in a system, process, or person that could be exploited. An attack is what happens when someone actually uses that weakness to cause harm.”

Types of Vulnerabilities:

Software Vulnerabilities:
“Bugs, unpatched systems, or outdated software that hackers can exploit.”
Hardware Vulnerabilities:
“Issues like insecure IoT devices or poorly configured routers.”
Human Vulnerabilities:
“People are predictable. Phishing, social engineering, and carelessness are easy to exploit.”
Types of Attacks:

“Attacks range from malware and phishing to brute force and denial-of-service attacks. Each one takes advantage of a specific type of vulnerability.”
Common Vulnerabilities at the Diamond
Lester pointed to a flowchart showing potential weak points in the casino’s systems. “Here’s what we’re dealing with.”

Unpatched Software:

“Every update they skip is an open door for attackers.”
Weak Passwords:

“If even one employee uses ‘password123,’ it could be game over.”
Misconfigured Systems:

“Firewalls, access controls—if they’re not set up properly, we can walk right through.”
IoT Device Exploits:

“Their cameras and slot machines are connected to the network. If one of them has a flaw, we’re in.”
Insider Threats:

“A disgruntled employee or careless contractor can be just as dangerous as a hacker.”
Attack Techniques
Lester clicked to a new slide, showing a list of attacks that could target these vulnerabilities. “Now, let’s talk about how an attacker might exploit these weaknesses.”

Phishing:

“Send an email pretending to be from IT. Get someone to click a malicious link, and boom—credentials stolen.”
Brute Force Attacks:

“Try every possible password until you get the right one. Automated tools can crack weak passwords in minutes.”
Denial-of-Service (DoS):

“Flood a system with traffic until it crashes. Imagine all their reservation systems going offline at once.”
Man-in-the-Middle (MITM):

“Intercept communications between devices. If we get into their network, we can eavesdrop on everything.”
Exploitation of Zero-Day Vulnerabilities:

“These are flaws no one knows about yet. If we can find one, they’ll never see it coming.”
How They Protect Against Attacks
Lester sighed, tapping his cane against the floor. “Of course, the Diamond isn’t clueless. They’ve got defenses in place for most of this.”

Patch Management:

“They update their systems regularly—at least, they’re supposed to.”
Multi-Factor Authentication (MFA):

“Even if we steal a password, we’ll need a second form of verification.”
Network Monitoring:

“Their intrusion detection systems will flag anything suspicious, like unusual traffic or failed logins.”
Employee Training:

“They train their staff to recognize phishing and social engineering attempts. Unfortunately for them, training isn’t foolproof.”
Weak Points in Their Defenses
Lester grinned, leaning closer to the screen. “But even the best defenses have gaps.”

Delayed Patching:

“Even if they update regularly, there’s always a delay between discovering a vulnerability and applying the patch.”
Careless Employees:

“Not everyone pays attention to training. It only takes one mistake.”
IoT Devices:

“These are harder to secure, and they’re often overlooked during audits.”
Attack Overload:

“If we hit them with multiple attacks at once, their systems might not catch everything.”
How We Exploit It
Lester’s smirk widened as he addressed the crew. “Here’s how we turn their vulnerabilities into opportunities.”

Find Unpatched Systems:

“Scan for software that hasn’t been updated. Even a minor flaw could be our way in.”
Phish the Right Person:

“Target employees with high access. If we get their credentials, we own their permissions.”
Overwhelm Their Defenses:

“Hit them with a denial-of-service attack while slipping something through the back door.”
Exploit IoT Blind Spots:

“Their cameras and slot machines are weak points. If we compromise one, we could pivot to the rest of the network.”  """)
    input("Press Enter To Return To The Menu")

def vocabulary17():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Vulnerabilities---"
        "Vulnerability": "A weakness in a system, process, or person that can be exploited.",
        "Software Vulnerabilities": "Flaws in code, such as unpatched systems or outdated software, that attackers can exploit.",
        "Hardware Vulnerabilities": "Security weaknesses in physical devices like routers or IoT systems.",
        "Human Vulnerabilities": "Weaknesses in people, including susceptibility to phishing and social engineering.",
        "Unpatched Software": "Programs that have not been updated to fix known flaws.",
        "Weak Passwords": "Easily guessable or common passwords that can be cracked through brute force.",
        "Misconfigured Systems": "Incorrectly set up systems, such as firewalls or access controls, that leave gaps in security.",
        "IoT Device Exploits": "Attacks targeting internet-connected devices like cameras or sensors.",
        "Insider Threats": "Risks posed by employees or contractors with access to sensitive systems.",

        "--_Attacks---"
        "Phishing": "Tricking users into revealing sensitive information through fake emails or websites.",
        "Brute Force Attacks": "Trying every possible password combination until the correct one is found.",
        "Denial-of-Service (DoS)": "Overloading a system with traffic to make it unavailable.",
        "Man-in-the-Middle (MITM)": "Intercepting communications between two parties to steal or manipulate data.",
        "Zero-Day Vulnerabilities": "Flaws that are unknown to the system’s developers and have no patch available.",

        "---Defenses---"
        "Patch Management": "The process of updating systems to fix known vulnerabilities.",
        "Multi-Factor Authentication (MFA)": "A security system that requires two or more forms of verification.",
        "Network Monitoring": "Continuous observation of network activity to detect and respond to threats.",
        "Employee Training": "Programs designed to educate employees on recognizing and avoiding cyber threats.",

        "---Weaknesses---"
        "Delayed Patching": "The time lag between discovering a vulnerability and applying a fix.",
        "Careless Employees": "Staff who ignore security protocols or fall for phishing scams.",
        "IoT Devices": "Devices connected to the internet that are often insecure and overlooked.",
        "Attack Overload": "Overwhelming a system with multiple attacks to bypass its defenses.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu18():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section18()
        elif choice == "2":
            vocabulary18()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section18():
    print("\n-- Content Section --")
    type_out(""" What is Malicious Activity?
Lester tapped his cane against the floor. “Malicious activity is the execution of an attacker’s plan. It’s how they exploit the vulnerabilities we talked about earlier to cause harm.”

Types of Malicious Activity:
Data Breaches:
“Stealing sensitive data like customer information or financial records.”
Ransomware:
“Encrypting systems or data and demanding payment to unlock it.”
System Sabotage:
“Destroying or altering systems to disrupt operations.”
Exfiltration:
“Secretly copying data without anyone noticing.”
Tactics Used in Malicious Activity
Lester pulled up a diagram of a typical attack lifecycle. “Malicious actors don’t just jump in guns blazing. They’re methodical.”

Lateral Movement:

“Once inside, attackers move from one system to another, looking for more valuable targets.”
Privilege Escalation:

“They find ways to upgrade their access—from a basic user to an admin account.”
Covering Tracks:

“Deleting logs, disabling alerts—anything to erase their digital footprints.”
Persistence:

“Setting up backdoors or installing malware to maintain long-term access.”
The Diamond’s Defenses Against Malicious Activity
Lester sighed, his tone darkening. “The Diamond Casino knows these tactics well. They’ve built layers of defense to stop this kind of activity.”

Data Loss Prevention (DLP):

“Monitors for unusual data transfers and blocks anything suspicious.”
Endpoint Security:

“Every device is locked down with antivirus software, firewalls, and EDR solutions.”
Log Analysis:

“Their SIEM systems continuously analyze logs for signs of malicious behavior.”
Behavioral Analytics:

“They watch for deviations from normal activity—like an employee accessing files they don’t normally touch.”
Weak Points in Their Defenses
Lester smirked, leaning forward. “But no system is foolproof. Even the Diamond’s defenses have gaps.”

Overwhelmed Systems:

“Their monitoring tools generate thousands of alerts daily. Important ones can get buried.”
Blind Spots in DLP:

“Some types of data exfiltration—like over encrypted channels—can bypass their detection.”
Human Blindness:

“Logs are only as useful as the people reviewing them. Miss one anomaly, and it’s game over for them.”
Delayed Response Times:

“Even with automation, some incidents take minutes—or longer—to investigate. That’s our window.”
How We Exploit It
Lester’s voice took on a conspiratorial tone. “Here’s how we use malicious activity to our advantage.”

Lateral Movement:

“Once we’re inside, we pivot from less secure systems to the crown jewels—their payment servers or vault access.”
Set Up Persistence:

“Install backdoors or sleeper agents in their systems. Even if they kick us out, we can come back.”
Exploit Overwhelmed Systems:

“Flood their monitoring tools with fake alerts. They’ll spend hours chasing ghosts while we do the real damage.”
Data Exfiltration:

“Steal data slowly, in small chunks, to avoid triggering alarms.”
Lester’s Final Thoughts
Lester turned back to the crew, his expression calm but confident. “Malicious activity is all about playing the long game. It’s not just about breaking in—it’s about staying in, doing damage, and leaving no trace. If we’re smart, the Diamond won’t even know what hit them until it’s too late.”  """)
    input("Press Enter To Return To The Menu")

def vocabulary18():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Malicious Activity---"
        "Malicious Activity": "Actions taken by an attacker to exploit vulnerabilities and cause harm or disruption.",
        "Data Breaches": "The unauthorized access and theft of sensitive data from an organization.",
        "Ransomware": "A type of malware that encrypts files or systems, demanding payment for decryption.",
        "System Sabotage": "Deliberate actions to destroy or disrupt systems, rendering them unusable.",
        "Exfiltration": "The unauthorized transfer of data out of a network or system.",

        "---Tactics---"
        "Lateral Movement": "The process of moving through a network from one system to another to find valuable targets.",
        "Privilege Escalation": "Gaining higher levels of access or permissions than originally granted.",
        "Covering Tracks": "Actions taken to hide evidence of malicious activity, such as deleting logs.",
        "Persistence": "Establishing long-term access to a system, often through backdoors or malware.",

        "---Defenses Against Malicious Activity---"
        "Data Loss Prevention (DLP)": "Technology that detects and prevents unauthorized data transfers.",
        "Endpoint Security": "Protections applied to individual devices, including antivirus software and firewalls.",
        "Log Analysis": "The review and interpretation of system logs to identify signs of malicious behavior.",
        "Behavioral Analytics": "Monitoring user actions to detect deviations from normal behavior.",

        "---Weaknesses in Defenses---"
        "Overwhelmed Systems": "Monitoring tools that generate too many alerts, making it easy to miss important ones.",
        "Blind Spots in DLP": "Data exfiltration methods that avoid detection, such as encrypted traffic.",
        "Human Blindness": "The inability of analysts to recognize critical anomalies within large volumes of data.",
        "Delayed Response Times": "The time lag between detecting an incident and initiating a response.",

        "---Exploitation Strategies---"
        "Lateral Movement": "Targeting less secure systems to pivot toward critical assets.",
        "Set Up Persistence": "Installing backdoors or malware to ensure continued access.",
        "Exploit Overwhelmed Systems": "Flooding monitoring tools with false alerts to hide real attacks.",
        "Data Exfiltration": "Stealing data in small increments to avoid detection by monitoring systems.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu19():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section19()
        elif choice == "2":
            vocabulary19()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()         

def content_section19():
    print("\n-- Content Section --")
    type_out(""" “The Diamond didn’t spend all this money just to look fancy. They’ve hardened their systems, their devices, and even their people. Hardening is about removing every unnecessary vulnerability. It’s their way of saying, ‘Good luck finding a crack.’ And our job? Find that crack.”

What is Hardening?
Lester tapped his cane as he spoke. “Hardening means making something as secure as possible by removing unnecessary risks.”

System Hardening:

“Locking down operating systems, removing unused features, and closing open ports. Anything they don’t need gets cut.”
Application Hardening:

“Configuring software to run securely. That means no default settings, no easy access.”
Network Hardening:

“Firewalls, encryption, and access control lists—every part of the network is configured to block attacks.”
Physical Hardening:

“Locks, fences, biometric scanners—they’ve locked down the building as much as the systems.”
Common Hardening Techniques
Lester brought up a slide listing the casino’s likely strategies. “Here’s what we’re up against.”

Patch Management:

“Every system is updated to fix known vulnerabilities.”
Configuration Baselines:

“They’ve got standard setups for every device and system. Any deviation gets flagged.”
Application Whitelisting:

“Only approved programs can run on their systems. Everything else is blocked.”
Encryption Everywhere:

“From their databases to their network traffic, everything is encrypted.”
Access Control:

“They’ve limited who can do what, and every action is logged.”
Advanced Hardening Measures
Lester clicked to another slide, showing the more sophisticated defenses the casino likely employs.

Disable Unnecessary Services:

“If they’re not using it, it’s off. No unused programs or open ports.”
Secure Boot:

“Their systems only load trusted software during startup.”
Endpoint Detection and Response (EDR):

“Constantly scans for threats and unusual activity on their devices.”
Remote Wipe:

“If a device is compromised or stolen, they can erase it remotely.”
Hardened IoT Devices:

“Every camera, slot machine, and thermostat is configured for security.”
How Hardening Stops Us
Lester sighed, crossing his arms. “Here’s why this makes our job harder.”

Minimal Attack Surface:

“By removing unnecessary features, they’ve reduced the number of ways we can get in.”
Strict Monitoring:

“Every change, every action is logged and reviewed.”
No Default Settings:

“Nothing is left in its default state, so there are no easy exploits.”
Real-Time Threat Detection:

“EDR and other tools mean they’ll catch us the second we do something suspicious.”
Weak Points in Hardening
Lester smirked, his confidence returning. “But no hardening is perfect. Even the best defenses have cracks.”

Human Error:

“The weakest link is always the people managing the systems.”
Inconsistent Updates:

“If they miss even one patch, it’s a vulnerability we can exploit.”
Neglected Devices:

“Old IoT devices or less critical systems might not be as secure as the rest.”
Complex Configurations:

“The more they harden, the more complex their setups get—and complexity breeds mistakes.”
How We Exploit It
Lester leaned on the table, his voice low but resolute. “Here’s how we turn their hardening against them.”

Find Unpatched Systems:

“If even one system is out of date, that’s our entry point.”
Look for Overlooked Devices:

“Target IoT devices or secondary systems they didn’t harden properly.”
Trick the People:

“Social engineering can bypass even the most hardened system. People are always the weakest link.”
Exploit Configuration Errors:

“Scan for misconfigurations. One bad setting could undo all their hard work.”  """)
    input("Press Enter To Return To The Menu")

def vocabulary19():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Hardening---"
        "Hardening": "The process of strengthening systems, devices, and networks to reduce vulnerabilities.",
        "System Hardening": "Securing operating systems by removing unused features, closing open ports, and applying updates.",
        "Application Hardening": "Configuring software to operate securely, removing default settings, and limiting access.",
        "Network Hardening": "Using firewalls, encryption, and access control lists to secure a network.",
        "Physical Hardening": "Strengthening physical security with locks, fences, and biometric controls.",

        "---Common Techniques----"
        "Patch Management": "The process of applying updates to fix known vulnerabilities in systems and applications.",
        "Configuration Baselines": "Standardized setups for systems and devices to ensure consistent security.",
        "Application Whitelisting": "Restricting systems to only run approved applications.",
        "Encryption Everywhere": "Using encryption to secure data at rest and in transit.",
        "Access Control": "Limiting access to systems and data based on user roles and logging all actions.",

        "---Advanced Measures---"
        "Disable Unnecessary Services": "Turning off unused programs or features to reduce potential vulnerabilities.",
        "Secure Boot": "Ensuring only trusted software loads during system startup.",
        "Endpoint Detection and Response (EDR)": "Tools that monitor and detect threats on devices in real time.",
        "Remote Wipe": "The ability to erase data from a device remotely in case of compromise.",
        "Hardened IoT Devices": "Configuring internet-connected devices to minimize security risks.",

        "---Challenges and Weak Points---"
        "Minimal Attack Surface": "The reduced number of potential entry points for attackers due to hardening.",
        "Strict Monitoring": "Continuous logging and reviewing of actions to detect unauthorized activity.",
        "No Default Settings": "Eliminating default configurations to avoid easy exploits.",
        "Human Error": "Mistakes made by administrators or users that undermine security.",
        "Inconsistent Updates": "Missed or delayed patches that leave systems vulnerable.",
        "Neglected Devices": "Less critical or older systems that may not receive the same security focus.",
        "Complex Configurations": "The increased likelihood of errors due to intricate system setups.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu20():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section20()
        elif choice == "2":
            vocabulary20()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section20():
    print("\n-- Content Section --")
    type_out("""  “Alright, team,” he began. “The Diamond Casino has thrown everything at us, from hardened systems to cutting-edge tech. But now we’re looking at the glue that holds it all together: their security techniques. These are the strategies and methods they use to keep us—and anyone else—from ever getting close to their assets.”

He tapped the laptop, and a complex chart of security protocols filled the screen.

What Are Security Techniques?
Lester pointed to the chart. “Think of security techniques as the playbook. They’re not just tools or systems—they’re the processes, strategies, and methods that bring everything together.”

Proactive Techniques:

“Techniques designed to prevent issues before they happen.”
Reactive Techniques:

“Methods for responding to threats or incidents after they occur.”
Proactive Security Techniques
Lester clicked to the next slide, outlining the Diamond’s likely proactive measures. “Here’s what they’re doing to stop us before we even make a move.”

Threat Hunting:

“Their teams are constantly searching for threats, even ones that haven’t triggered alarms yet.”
Network Segmentation:

“Breaking the network into smaller sections to limit the damage an attacker can do.”
User Training:

“Their employees are trained to recognize phishing, social engineering, and other common tactics.”
Access Reviews:

“Regularly checking who has access to what and revoking permissions that aren’t needed.”
Reactive Security Techniques
The crew groaned as Lester brought up another set of slides, this time focused on reactive measures.

Incident Response:

“When something goes wrong, they have a playbook ready to isolate, contain, and recover.”
Forensic Analysis:

“After an incident, they dig through the evidence to figure out what happened—and who’s responsible.”
Rollback Strategies:

“If their systems get hit with ransomware or a bad update, they can roll back to a previous state.”
Threat Intelligence Updates:

“They adjust their defenses in real-time based on the latest threat information.”
Advanced Security Techniques
Lester flipped to the next slide, showing some of the more sophisticated strategies in play. “And then there are the big guns.”

Deception Technology:

“They might have honeypots—fake systems designed to attract attackers and study their methods.”
Behavioral Analytics:

“Analyzing user behavior to detect anomalies, like logging in at odd hours or accessing unusual files.”
Zero Trust Architecture:

“No one—employee or system—is trusted by default. Every action is verified.”
Security Orchestration, Automation, and Response (SOAR):

“Automated tools that detect and respond to threats faster than any human could.”
How Security Techniques Stop Us
Lester leaned forward, his tone serious. “This is what makes the Diamond so tough to crack.”

Real-Time Response:

“Their systems can detect and react to threats instantly.”
Minimal Access Points:

“By segmenting their network and limiting permissions, they’ve shrunk their attack surface.”
Dynamic Adjustments:

“They’re constantly learning and adapting based on new threats.”
Comprehensive Recovery:

“Even if we break something, they can restore it before we get away with anything.”
Exploiting Weak Points
Lester’s grin returned as he clicked to the final slide. “But even the best techniques have their flaws.”

Overconfidence:

“They might rely too heavily on automation, thinking their systems can handle everything.”
Gaps in Training:

“No training program is perfect. Some employees will always slip up.”
Blind Spots:

“Even the best monitoring tools miss things, especially in complex systems.”
Delayed Responses:

“If their automation doesn’t catch something, they’ll need time to investigate—and that’s our window.”
Lester’s Final Thoughts
Lester turned back to face the crew. “The Diamond Casino didn’t just build a secure system—they built a strategy. But every strategy has weak points, and every technique has limits. If we’re methodical, precise, and just a little lucky, we’ll beat them at their own game.”

 """)
    input("Press Enter To Return To The Menu")

def vocabulary20():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Security Techniques---"
        "Security Techniques": "Strategies and methods used to protect systems, data, and networks from threats.",
        "Proactive Techniques": "Measures taken to prevent threats before they occur.",
        "Reactive Techniques": "Methods used to respond to and mitigate threats after they occur.",

        "---Proactive Security Techniques---"
        "Threat Hunting": "Actively searching for potential threats that have not triggered alerts.",
        "Network Segmentation": "Dividing a network into smaller sections to limit the spread of an attack.",
        "User Training": "Educating employees to recognize and avoid security threats like phishing.",
        "Access Reviews": "Regularly auditing permissions to ensure users only have access to what they need.",

        "---Reactive Security Techniques---"
        "Incident Response": "A structured approach to detecting, containing, and recovering from security incidents.",
        "Forensic Analysis": "Examining logs and evidence to determine the cause and scope of an attack.",
        "Rollback Strategies": "Reverting systems to a previous state to undo damage caused by an attack.",
        "Threat Intelligence Updates": "Adjusting defenses based on the latest information about threats.",

        "---Advanced Security Techniques---"
        "Deception Technology": "Using fake systems or data to lure attackers and study their methods.",
        "Behavioral Analytics": "Monitoring user behavior to detect unusual or suspicious activity.",
        "Zero Trust Architecture": "A security model where no user or system is trusted by default, and every action is verified.",
        "Security Orchestration, Automation, and Response (SOAR)": "Automated tools that detect and respond to threats in real-time.",

        "---Challenges and Weak Points---"
        "Overconfidence": "Relying too heavily on automation or tools, leading to complacency.",
        "Gaps in Training": "Inconsistent or insufficient employee training, leading to human errors.",
        "Blind Spots": "Areas of a system or network that are not adequately monitored or protected.",
        "Delayed Responses": "The time lag between detecting and responding to a threat, allowing attackers a window of opportunity.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu21():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section21()
        elif choice == "2":
            vocabulary21()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section21():
    print("\n-- Content Section --")
    type_out(""" “Alright,” he began. “We’ve talked about vulnerabilities before—those little cracks in the system. But here’s the thing: the Diamond doesn’t just wait for someone to find them. They’ve got an entire process dedicated to sniffing out vulnerabilities before anyone else can. It’s called vulnerability management, and it’s our next big hurdle.”

What is Vulnerability Management?
Lester tapped his cane as he spoke. “Vulnerability management isn’t just finding flaws—it’s a continuous cycle. They don’t stop at discovery; they track, assess, and fix them.”

Discovery:

“First step: figure out where the vulnerabilities are. They scan their systems, devices, and networks constantly.”
Assessment:

“Next, they prioritize the risks. Not every vulnerability is critical—they decide which ones to patch first.”
Remediation:

“Then, they fix the problem. Patching software, updating configurations—whatever it takes.”
Verification:

“Finally, they test to make sure the fix worked. No point in patching if the hole’s still there.”
The Vulnerability Management Lifecycle
Lester flipped to a new slide showing a cycle diagram. “Here’s how they stay one step ahead.”

Asset Inventory:

“You can’t secure what you don’t know exists. They keep a detailed inventory of every system and device.”
Vulnerability Scanning:

“Their tools automatically scan for weak points, like unpatched software or misconfigured firewalls.”
Risk Assessment:

“Once vulnerabilities are found, they rank them based on how dangerous they are.”
Patch Management:

“They deploy updates regularly to close those gaps.”
Reporting and Metrics:

“They track everything—what was found, what was fixed, and what’s still pending.”
Tools and Techniques for Vulnerability Management
Lester clicked to another slide, listing the Diamond’s likely tools. “This is what they’re probably using.”

Vulnerability Scanners:

“Automated tools like Nessus or Qualys scan their network for flaws.”
Configuration Management:

“Tools that compare systems to a baseline to spot misconfigurations.”
Patch Management Systems:

“Centralized platforms for deploying updates across all devices.”
Threat Intelligence Integration:

“They pull in real-time data about new vulnerabilities and attacks.”
Penetration Testing:

“Ethical hackers simulate attacks to test their defenses.”
How Vulnerability Management Stops Us
Lester sighed, pacing in front of the crew. “Here’s why this makes our job harder.”

Constant Monitoring:

“They’re always scanning, so any weakness we exploit might get patched before we can use it.”
Prioritized Fixes:

“They focus on the most dangerous vulnerabilities first, leaving fewer openings for us.”
Proactive Defense:

“They’re not waiting for an attack—they’re actively looking for ways to stop one.”
Comprehensive Coverage:

“Every server, every camera, every system is on their radar.”
Weaknesses in Vulnerability Management
Lester smirked, turning to the final slide. “But even the best vulnerability management has cracks.”

Delayed Patching:

“Fixing vulnerabilities takes time. If we strike before the patch, we’re in.”
Missed Assets:

“If they don’t inventory everything—like IoT devices—we can exploit what they miss.”
False Sense of Security:

“They might rely too heavily on scanning tools, ignoring human creativity.”
Unpatched Low-Risk Issues:

“Not every vulnerability gets patched, especially if it’s deemed ‘low-risk.’ That’s where we strike.”
How We Exploit It
Lester’s tone turned conspiratorial as he outlined their plan. “Here’s how we make their vulnerability management work for us.”

Focus on Missed Assets:

“Find the devices or systems they didn’t scan—IoT devices are a great target.”
Exploit Delayed Patching:

“If we know about a vulnerability before they patch it, we move fast.”
Test Low-Risk Issues:

“If they ignored a vulnerability because it seemed minor, we see if it can be escalated.”
Use Zero-Days:

“If we can find a zero-day vulnerability, their scanners won’t catch it.”
Lester’s Final Thoughts
Lester leaned on the table, his voice firm. “The Diamond’s vulnerability management is like a tightrope act. They’re always one step away from falling off. If we’re smart, we’ll find the gaps they missed. And when we do, this heist is ours.”

  """)
    input("Press Enter To Return To The Menu")

def vocabulary21():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Vulnerability Management---"
        "Vulnerability Management": "The continuous process of identifying, assessing, and remediating security vulnerabilities.",
        "Discovery": "Identifying vulnerabilities through scanning and inventorying systems.",
        "Assessment": "Evaluating vulnerabilities to prioritize which ones to address first.",
        "Remediation": "Taking steps to fix vulnerabilities, such as patching or reconfiguring systems.",
        "Verification": "Testing to ensure that remediated vulnerabilities are properly fixed.",

        "---Lifecycle Steps---"
        "Asset Inventory": "Maintaining a detailed list of all hardware, software, and network devices in an organization.",
        "Vulnerability Scanning": "Using automated tools to identify weaknesses in systems or networks.",
        "Risk Assessment": "Ranking vulnerabilities based on their potential impact and likelihood of exploitation.",
        "Patch Management": "Deploying updates to software or systems to close security gaps.",
        "Reporting and Metrics": "Tracking and documenting vulnerabilities, fixes, and remaining risks.",

        "---Tools and Techniques---"
        "Vulnerability Scanners": "Automated tools like Nessus or Qualys that identify potential weaknesses.",
        "Configuration Management": "Ensuring systems match security baselines and identifying deviations.",
        "Patch Management Systems": "Platforms that automate the deployment of updates across devices.",
        "Threat Intelligence Integration": "Incorporating real-time information about emerging vulnerabilities and threats.",
        "Penetration Testing": "Simulated attacks by ethical hackers to test an organization’s defenses.",

        "---Weak Points---"
        "Delayed Patching": "The time lag between identifying a vulnerability and applying a fix.",
        "Missed Assets": "Systems or devices that are not included in vulnerability scans.",
        "False Sense of Security": "Overreliance on automated tools, ignoring potential human creativity in attacks.",
        "Unpatched Low-Risk Issues": "Vulnerabilities deemed minor and left unfixed, which can still be exploited.",

        "---Exploitation Strategies---"
        "Focus on Missed Assets": "Targeting devices or systems that were not included in scans.",
        "Exploit Delayed Patching": "Taking advantage of the window before a vulnerability is patched.",
        "Test Low-Risk Issues": "Exploring seemingly minor vulnerabilities to find ways to escalate their impact.",
        "Use Zero-Days": "Exploiting vulnerabilities that are unknown to the vendor and have no patch available.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu22():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section22()
        elif choice == "2":
            vocabulary22()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section22():
    print("\n-- Content Section --")
    type_out(""" What Are Alerting and Monitoring?
Lester tapped his cane for emphasis. “Alerting and monitoring are how the casino detects threats and acts on them. Monitoring watches everything, while alerting makes sure the right people know when something goes wrong.”

Monitoring:

“This is continuous observation of systems, networks, and users. Think of it as their eyes and ears.”
Alerting:

“When monitoring detects something suspicious, alerting is the messenger that screams for help.”
Core Components of Alerting and Monitoring
Lester clicked to the next slide, highlighting the key tools and processes the casino likely employs.

SIEM (Security Information and Event Management):

“This is the brain of their monitoring system. It collects data from all over the network, analyzes it, and generates alerts.”
Log Management:

“Every action on their systems is logged. If someone opens a door, logs in, or even hovers over a file, it’s recorded.”
Real-Time Alerts:

“If something suspicious happens—like multiple failed logins or unusual data transfers—the system flags it immediately.”
Behavioral Analytics:

“They’re not just looking for known threats. Their systems analyze patterns to catch anomalies.”
Network Traffic Analysis:

“Every packet of data flowing in or out of their network is monitored for unusual activity.”
Advanced Monitoring Techniques
Lester smirked as he showed another slide, this one filled with the casino’s cutting-edge strategies.

Threat Intelligence Feeds:

“They integrate real-time updates about emerging threats into their systems.”
Endpoint Detection and Response (EDR):

“Every device is monitored for unusual behavior, like unauthorized software or strange file activity.”
Deception Technology:

“They might have honeypots—fake systems designed to lure attackers and study their methods.”
AI and Machine Learning:

“Their monitoring systems are smart. They learn from past incidents to predict and stop new ones.”
How Alerting and Monitoring Stop Us
Lester’s tone grew serious as he addressed the crew. “Here’s why this makes our job harder.”

Immediate Detection:

“If we make one wrong move, the system will know.”
Contextual Alerts:

“Their systems don’t just detect anomalies—they understand the context. A failed login might be ignored, but ten in a row? That’s a red flag.”
Comprehensive Coverage:

“Every corner of their network is monitored. There are no blind spots.”
Automated Responses:

“Some alerts trigger immediate actions, like locking accounts or isolating systems.”
Weak Points in Alerting and Monitoring
Lester’s grin returned as he clicked to the next slide. “But even the best systems have weak points.”

Alert Fatigue:

“When they get too many alerts, important ones might get overlooked.”
False Positives:

“Not every alert is a real threat. If their system cries wolf too often, people stop listening.”
Delayed Analysis:

“Some alerts require human review. That takes time, and that’s our window.”
Overreliance on Automation:

“Their systems are only as good as their programming. A clever attack might slip through.”
How We Exploit It
Lester leaned forward, his voice dripping with confidence. “Here’s how we use their alerting and monitoring against them.”

Flood the System:

“Overwhelm their monitoring tools with fake alerts. Make them chase ghosts while we do the real work.”
Exploit Blind Spots:

“Find areas they’re not watching closely—like IoT devices or older systems.”
Delay Responses:

“Trigger low-priority alerts to distract their analysts and buy us time.”
Avoid Detection:

“Keep our movements subtle. Stay under the radar, and their alerts won’t even go off.”
Lester’s Final Thoughts
Lester straightened up, his tone resolute. “The Diamond Casino’s alerting and monitoring are state-of-the-art. But no system is perfect. If we’re patient, precise, and just a little lucky, we can slip through their defenses. Let’s make it happen.”

  """)
    input("Press Enter To Return To The Menu")

def vocabulary22():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Alerting and Monitoring---"
        "Alerting and Monitoring": "Processes used to detect and respond to potential threats by continuously observing systems and generating alerts.",
        "Monitoring": "Continuous observation of networks, systems, and user activities to identify anomalies.",
        "Alerting": "The process of notifying relevant personnel or systems when a potential threat is detected.",

        "---Core Components---"
        "SIEM (Security Information and Event Management)": "A system that collects, analyzes, and generates alerts from network and system data.",
        "Log Management": "The process of collecting and storing logs of all actions performed within systems.",
        "Real-Time Alerts": "Immediate notifications triggered by suspicious or unusual activity.",
        "Behavioral Analytics": "Analyzing user and system behavior to detect anomalies.",
        "Network Traffic Analysis": "Monitoring data packets flowing through a network to identify unusual patterns.",

        "---Advanced Techniques---"
        "Threat Intelligence Feeds": "Real-time updates about emerging threats integrated into monitoring systems.",
        "Endpoint Detection and Response (EDR)": "Monitoring devices for unusual activity and providing tools to respond to incidents.",
        "Deception Technology": "Using honeypots or decoy systems to lure attackers and study their methods.",
        "AI and Machine Learning": "Using smart systems that learn from past incidents to predict and detect threats.",

        "---Challenges and Weak Points---"
        "Alert Fatigue": "When too many alerts overwhelm personnel, leading to important ones being missed.",
        "False Positives": "Alerts that flag legitimate activity as suspicious, wasting time and resources.",
        "Delayed Analysis": "The time it takes for humans to review and respond to certain alerts.",
        "Overreliance on Automation": "Dependence on automated systems that may fail to detect sophisticated or novel threats.",

        "---Exploitation Strategies---"
        "Flood the System": "Overloading monitoring tools with fake alerts to distract analysts.",
        "Exploit Blind Spots": "Finding areas of the network or systems that are not closely monitored.",
        "Delay Responses": "Triggering low-priority alerts to occupy analysts and create opportunities.",
        "Avoid Detection": "Conducting activities in a subtle way to stay under the radar of monitoring systems.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu23():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section23()
        elif choice == "2":
            vocabulary23()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section23():
    print("\n-- Content Section --")
    type_out(""" What is Incident Response?
Lester pointed to the flowchart. “Incident response is their playbook for dealing with trouble. It’s not just about reacting—it’s about controlling the situation.”

Incident Response:

“A structured process for identifying, managing, and resolving security incidents.”
Incident:

“Any event that disrupts or threatens their systems, whether it’s a malware infection, a DDoS attack, or, well... us.”
The Phases of Incident Response
Lester clicked through the chart, walking the crew through each phase. “They’ll follow these steps like clockwork.”

Preparation:

“They’ve got policies, tools, and teams in place before anything happens.”
Identification:

“The moment something looks off, they investigate to confirm it’s an incident.”
Containment:

“Once they know what’s happening, they isolate the affected systems to stop the damage from spreading.”
Eradication:

“Next, they remove the threat—whether it’s malware, compromised accounts, or unauthorized devices.”
Recovery:

“After fixing the issue, they restore normal operations, making sure everything is secure.”
Lessons Learned:

“Finally, they review what happened and make changes to prevent it from happening again.”
Tools and Teams in Incident Response
Lester switched to the next slide, showcasing the people and tools involved. “This isn’t just about tech—it’s about coordination.”

Incident Response Team (IRT):

“A dedicated group trained to handle emergencies. They’re fast, focused, and ruthless.”
Security Information and Event Management (SIEM):

“Their SIEM tools gather data from across the network to detect and analyze incidents.”
Forensic Tools:

“Used to investigate what went wrong and trace the source of the problem.”
Threat Intelligence Feeds:

“They pull in real-time updates about new threats to adapt their response.”
Communication Plans:

“They’ve got scripts ready for notifying staff, customers, and even law enforcement if needed.”
How Incident Response Stops Us
Lester sighed, pacing in front of the screen. “This is what makes their system so hard to beat.”

Speed:

“Their team is trained to act fast—minutes, not hours.”
Coordination:

“Every department knows their role. There’s no confusion, no hesitation.”
Isolation Tactics:

“They can cut off compromised systems before we have a chance to spread the damage.”
Post-Incident Analysis:

“Even if we get away, they’ll analyze everything to make sure it doesn’t happen again.”
Weak Points in Incident Response
Lester smirked, clicking to the next slide. “But even the best teams have flaws. Here’s where we might find our openings.”

Delayed Identification:

“If they don’t recognize the incident immediately, we’ll have extra time to operate.”
Human Error:

“No plan survives contact with reality. Someone might misjudge the situation.”
Overwhelmed Teams:

“If we create enough chaos, their team might struggle to keep up.”
Blind Spots:

“If they don’t see the full scope of the attack, their containment efforts might leave us a way out.”
How We Exploit It
Lester leaned on the table, his voice low but confident. “Here’s how we make their incident response work for us.”

Trigger Decoys:

“Set off fake alarms to distract their team while we hit the real target.”
Exploit Delayed Responses:

“If we move faster than they can, we’ll finish the job before they know what hit them.”
Leverage Human Error:

“Social engineering or clever misdirection can make their team second-guess themselves.”
Spread the Chaos:

“Attack multiple systems at once. Overwhelm their response team and slip through the cracks.”
Lester’s Final Thoughts
Lester turned back to the crew, his tone sharp. “Incident response is their ace in the hole. It’s designed to stop us cold. But if we’re faster, smarter, and just a little more creative, we can turn their strength into a weakness. Let’s make it happen.”  """)
    input("Press Enter To Return To The Menu")

def vocabulary23():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Incident Response---"
        "Incident Response": "A structured process for identifying, managing, and resolving security incidents.",
        "Incident": "Any event that disrupts or threatens normal operations, such as a malware infection or DDoS attack.",

        "---Phases of Incident Response---"
        "Preparation": "Establishing policies, tools, and teams before an incident occurs.",
        "Identification": "Detecting and confirming that an incident has occurred.",
        "Containment": "Isolating the affected systems to prevent the threat from spreading.",
        "Eradication": "Removing the threat from the environment, such as malware or unauthorized users.",
        "Recovery": "Restoring normal operations while ensuring the system is secure.",
        "Lessons Learned": "Reviewing the incident to improve defenses and prevent future occurrences.",

        "---Tools and Teams---"
        "Incident Response Team (IRT)": "A dedicated group responsible for managing and resolving incidents.",
        "Security Information and Event Management (SIEM)": "Tools that collect and analyze data to detect and respond to security incidents.",
        "Forensic Tools": "Software and techniques used to investigate and trace the source of security incidents.",
        "Threat Intelligence Feeds": "Real-time updates about emerging threats integrated into response efforts.",
        "Communication Plans": "Predefined scripts and protocols for notifying stakeholders during an incident.",

        "---Weak Points---"
        "Delayed Identification": "The time lag between an incident occurring and it being recognized.",
        "Human Error": "Mistakes made by individuals during the response process.",
        "Overwhelmed Teams": "Response teams struggling to keep up with multiple incidents or high-pressure situations.",
        "Blind Spots": "Areas of the system or attack that are not fully understood or addressed during the response.",

        "---Exploitation Strategies---"
        "Trigger Decoys": "Setting off fake alarms to distract response teams from the real attack.",
        "Exploit Delayed Responses": "Taking advantage of the time gap before an incident is identified and acted upon.",
        "Leverage Human Error": "Manipulating response team members to create confusion or mistakes.",
        "Spread the Chaos": "Attacking multiple systems to overwhelm the response team and create opportunities.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu24():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section24()
        elif choice == "2":
            vocabulary24()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section24():
    print("\n-- Content Section --")
    type_out(""" 
Lester’s Casino Heist: Investigating an Incident Casing

The crew was quiet, listening intently as Lester Crest brought up the next topic. The projector illuminated the room with the words “Investigating an Incident.” Lester’s face was calm but focused as he leaned on his cane.

“Alright,” he began, “here’s the deal. If we slip up, the Diamond Casino will turn everything they’ve got toward one goal: figuring out what happened and who’s responsible. That’s the purpose of an incident investigation. It’s not just about stopping us—it’s about learning every detail of how we pulled it off and making sure no one ever does it again.”

He tapped the keyboard, and a detailed diagram appeared, outlining the investigation process.

What is Incident Investigation?
Lester pointed to the diagram. “Investigating an incident is all about digging into the details. They’ll follow a trail to uncover every piece of evidence.”

Incident Investigation:

“A systematic process to identify the cause, scope, and impact of a security incident.”
Evidence Collection:

“Gathering data from systems, logs, and devices to piece together what happened.”
Analysis:

“Examining the evidence to determine the root cause and how the incident unfolded.”
Steps in Investigating an Incident
Lester walked the crew through the investigation process, highlighting each step.

Preservation of Evidence:

“The first thing they do is freeze everything. They don’t want logs overwritten or systems altered.”
Data Collection:

“They’ll pull logs, device snapshots, and network traffic to start building their case.”
Analysis:

“Here, they figure out what happened—how we got in, what we did, and what damage we caused.”
Attribution:

“This is where they try to trace the attack back to us—or make it look like someone else did it.”
Reporting:

“Finally, they document everything in painstaking detail for management, law enforcement, or regulators.”
Tools for Investigating an Incident
Lester clicked to the next slide, outlining the tools the casino likely has at its disposal. “This is the arsenal they’ll use to track us.”

Log Analysis Tools:

“They’ll go through system logs line by line, looking for anomalies.”
Network Forensics:

“Every packet of data that passed through their network is fair game.”
Endpoint Forensics:

“They’ll take snapshots of affected devices to analyze changes in files or memory.”
Malware Analysis:

“If we leave any malicious code behind, they’ll dissect it to figure out what it did and where it came from.”
SIEM (Security Information and Event Management):

“Their SIEM tools will correlate data from multiple sources to build a timeline of events.”
Challenges of Investigating an Incident
Lester paused, giving the crew a moment to absorb the information. “Here’s why this process is such a pain—for them and for us.”

Volume of Data:

“They’ll have to sift through mountains of logs and network traffic.”
Time Pressure:

“The longer it takes them to investigate, the greater the risk of further damage.”
Complex Attacks:

“If we play our cards right, the complexity of our attack will slow them down.”
Attribution Challenges:

“Making sure they can’t trace the attack back to us is half the battle.”
Weak Points in Incident Investigation
Lester smirked as he clicked to the final slide. “But even the best investigators have blind spots. Here’s where we can trip them up.”

Incomplete Data:

“If we erase key logs or use encryption, they won’t have the full picture.”
False Trails:

“We can plant misleading evidence to make it look like someone else was behind the attack.”
Tool Limitations:

“Some forensic tools can’t handle encrypted or obfuscated data.”
Human Error:

“If they miss one detail, the entire investigation could fall apart.”
How We Exploit It
Lester’s voice grew quieter, his tone conspiratorial. “Here’s how we make their investigation harder—and our exit cleaner.”

Cover Our Tracks:

“Delete logs, overwrite files, and leave no trace of how we got in.”
Use Encryption:

“Encrypt our communications and tools to prevent analysis.”
Plant Decoys:

“Leave behind fake data or evidence to send them chasing ghosts.”
Stay Unpredictable:

“Use unexpected techniques and patterns. If they can’t figure out our methods, they can’t stop us.”
Lester’s Final Thoughts
Lester leaned forward, his expression serious. “The Diamond’s investigators are sharp, but no investigation is perfect. If we’re careful, we can muddy the waters enough to escape clean. And once we’re out, there’s no way they’ll pin this on us.”  """)
    input("Press Enter To Return To The Menu")

def vocabulary24():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Incident Investigation---"
        "Incident Investigation": "A systematic process to identify the cause, scope, and impact of a security incident.",
        "Evidence Collection": "The process of gathering data from systems, logs, and devices to analyze an incident.",
        "Analysis": "Examining collected evidence to determine the root cause and the sequence of events.",

        "---Steps in Incident Investigation---"
        "Preservation of Evidence": "Ensuring that data related to the incident is not altered or overwritten.",
        "Data Collection": "Gathering logs, snapshots, and other relevant information for analysis.",
        "Attribution": "Determining who or what was responsible for the incident.",
        "Reporting": "Documenting the findings of the investigation in detail for stakeholders.",

        "---Tools for Investigation---"
        "Log Analysis Tools": "Software used to examine logs for anomalies and traces of malicious activity.",
        "Network Forensics": "The analysis of network traffic to uncover signs of an attack or data exfiltration.",
        "Endpoint Forensics": "Analyzing affected devices for changes in files, memory, or configurations.",
        "Malware Analysis": "Studying malicious code to understand its purpose and origin.",
        "SIEM (Security Information and Event Management)": "Tools that correlate and analyze data from multiple sources to build a timeline of events.",

        "---Challenges---"
        "Volume of Data": "The large amount of information investigators must analyze to find relevant evidence.",
        "Time Pressure": "The need to resolve the investigation quickly to prevent further damage.",
        "Complex Attacks": "Sophisticated techniques that make it difficult to piece together the sequence of events.",
        "Attribution Challenges": "The difficulty in identifying the true source of an attack, especially with false trails.",

        "---Weak Points---"
        "Incomplete Data": "Missing logs or encrypted communications that hinder analysis.",
        "False Trails": "Misleading evidence planted by attackers to confuse investigators.",
        "Tool Limitations": "The inability of forensic tools to analyze encrypted or obfuscated data.",
        "Human Error": "Mistakes made by investigators that can compromise the accuracy of their findings.",

        "---Exploitation Strategies---"
        "Cover Our Tracks": "Deleting or altering logs and evidence to hide the attacker’s presence.",
        "Use Encryption": "Encrypting communications and tools to prevent analysis.",
        "Plant Decoys": "Leaving fake evidence to mislead investigators.",
        "Stay Unpredictable": "Using unique techniques to avoid detection and analysis.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")
    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu25():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section25()
        elif choice == "2":
            vocabulary25()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section25():
    print("\n-- Content Section --")
    type_out("""  The screen lit up with the words “Automation and Orchestration,” framed by a sleek diagram of interconnected systems. Lester grinned.

“This,” he began, “is where things get high-tech. The Diamond doesn’t just rely on people—they’ve automated their defenses and orchestrated them to work together seamlessly. This isn’t just security; it’s a self-driving fortress. And that makes our job... complicated.”

What Are Automation and Orchestration?
Lester tapped his cane against the floor. “Automation is about speed and consistency. Orchestration is about coordination. Together, they turn a bunch of individual tools into a well-oiled machine.”

Automation:

“Repetitive tasks done by machines instead of people. Fast, efficient, and no coffee breaks.”
Orchestration:

“The integration of different tools and systems, making them work together like a symphony.”
How Automation and Orchestration Work
Lester clicked to a slide showing the flow of an automated response. “Let me break it down.”

Detection:

“The system detects a threat—malware, an intrusion, whatever.”
Alerting:

“An automated alert goes out to the right people—or even to other systems.”
Response:

“The system executes pre-defined actions, like isolating a compromised device.”
Follow-Up:

“Once the threat is contained, orchestration ensures everything gets logged, analyzed, and updated.”
Key Tools in Automation and Orchestration
Lester leaned on the table as he highlighted the Diamond’s likely setup. “These tools are what keep their defenses running like clockwork.”

Security Orchestration, Automation, and Response (SOAR):

“This is their control center. SOAR integrates all their tools and automates workflows.”
Playbooks:

“Predefined workflows that dictate how systems respond to specific threats.”
Threat Intelligence Platforms:

“These pull in real-time data about new threats and feed it directly into their defenses.”
Automated Incident Response:

“If something goes wrong, their systems act without waiting for a human.”
Integration Hubs:

“Tools like APIs connect their various systems, making sure everything communicates perfectly.”
How Automation and Orchestration Stop Us
Lester sighed, pacing as he spoke. “Here’s why this makes their defenses so tough.”

Speed:

“Machines don’t hesitate. They detect and respond faster than any human team.”
Consistency:

“No human error. The same actions are taken every time.”
Scalability:

“Whether it’s one alert or a hundred, their systems can handle it without breaking a sweat.”
Real-Time Updates:

“If a new threat emerges, their systems are updated instantly.”
Weak Points in Automation and Orchestration
Lester’s smirk returned as he brought up the final slide. “But no system is perfect—not even one this fancy.”

Overreliance on Automation:

“If something isn’t in their playbooks, the system won’t know how to handle it.”
Integration Errors:

“With so many systems working together, a misconfigured API or integration can create blind spots.”
Complexity:

“The more complex their orchestration, the more room there is for mistakes.”
False Positives:

“Automation isn’t perfect. If the system flags legitimate activity as a threat, it can cause delays.”
How We Exploit It
Lester turned to the crew, his tone sharp. “Here’s how we turn their automation and orchestration against them.”

Create Chaos:

“Flood their systems with fake threats. Let the automation bog itself down while we move in.”
Find Integration Gaps:

“Look for poorly connected systems. If something doesn’t communicate properly, we can exploit it.”
Use Novel Tactics:

“If we do something they haven’t seen before, their playbooks won’t know how to respond.”
Trigger False Positives:

“Force their automation to overreact. The more noise we create, the easier it is to slip through.”  """)
    input("Press Enter To Return To The Menu")

def vocabulary25():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Automation and Orchestration---"
        "Automation": "The use of machines to perform repetitive tasks without human intervention.",
        "Orchestration": "The integration and coordination of multiple tools and systems to work together effectively.",

        "---How It Works---"
        "Detection": "The process of identifying potential threats or anomalies in a system.",
        "Alerting": "Notifying relevant systems or personnel about a detected threat.",
        "Response": "Automated actions taken to mitigate or contain a threat.",
        "Follow-Up": "Post-incident actions like logging, analysis, and system updates.",

        "---Tools---"
        "Security Orchestration, Automation, and Response (SOAR)": "A platform that integrates security tools and automates workflows for faster incident response.",
        "Playbooks": "Predefined workflows that dictate automated responses to specific types of threats.",
        "Threat Intelligence Platforms": "Tools that collect and share real-time data about emerging threats.",
        "Automated Incident Response": "Automated processes that detect and respond to security incidents without human intervention.",
        "Integration Hubs": "Platforms or APIs that connect different security tools and systems to enable orchestration.",

        "---Challenges and Weak Points---"
        "Overreliance on Automation": "Dependence on predefined actions that may fail to handle novel threats.",
        "Integration Errors": "Misconfigurations or issues in connecting multiple systems that create blind spots.",
        "Complexity": "The difficulty in managing and maintaining intricate systems and workflows.",
        "False Positives": "Incorrectly flagged activity that appears suspicious but is legitimate.",

        "---Exploitation Strategies---"
        "Create Chaos": "Overloading automated systems with fake threats to slow down or disrupt operations.",
        "Find Integration Gaps": "Identifying poorly connected or misconfigured systems to exploit.",
        "Use Novel Tactics": "Employing methods or techniques that the automated systems are not programmed to handle.",
        "Trigger False Positives": "Forcing the system to react to harmless activity, creating delays and distractions.",
    }
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   
def submenu26():
    while True:
        print("\n--- Menu ---")
        print("1. Content ")
        print("2. Vocab ")
        print("3. Main Menu ")

        choice = input("Choose An Option: ")

        if choice == "1":
            content_section26()
        elif choice == "2":
            vocabulary26()
        elif choice == "3":
            display_menu()
            break
        else:
            print("Invalid option.")

def type_out(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def content_section26():
    print("\n-- Content Section --")
    type_out(""" Security Awareness and the Human Element
"First off," Lester began, pointing to a security training manual he'd hacked from the casino, "the casino staff undergoes security awareness training. That’s their first line of defense. They're trained to spot suspicious behavior and follow procedures to protect sensitive information."

"Like what?" asked the driver, slumped in a chair.

"Plenty," Lester replied. "They know about social engineering attacks—manipulative tricks to exploit their psychology. Ever try sweet-talking someone into letting you through a restricted area? These people have been taught to resist."

He rattled off examples:

Shoulder surfing: Watching over someone's shoulder to steal info.
Eavesdropping: Listening in on private conversations.
Dumpster diving: Searching through trash for sensitive data.
Insider Threats
"But it’s not just about outsiders," Lester continued. "The casino has systems to detect insider threats—employees who might misuse their access intentionally or by mistake. They’re on the lookout for staff showing behavior indicators, like financial struggles or odd, unauthorized data access."

"What about passwords?" the hacker asked, leaning forward.

Password Management
"Glad you asked," Lester said. "The casino uses top-tier password management policies. No writing down passwords. They enforce strong, unique combinations stored securely in password managers."

He held up a fake email he'd intercepted. "The staff even practice avoiding phishing scams, like this beauty. They’ll look for mismatched URLs or poor grammar and report it before clicking anything dangerous."

A Culture of Security
Lester smirked. "And here’s the kicker: they’ve built a culture of security. It’s drilled into them to treat every interaction as a potential breach. They don’t hold doors open for strangers—no piggybacking or tailgating into secure areas."

The room grew quiet as Lester listed the casino's meticulous policies:

Remote work protocols: No one accesses systems from unsecured networks.
Operational security (OPSEC): Staff avoid sharing sensitive info online or in casual conversation.
The safecracker looked nervous. "So they’ve thought of everything?"

"Not quite everything," Lester said, smirking. "But they’re pretty close. This isn’t just about cameras and locks—it’s about awareness, habits, and vigilance. And trust me, they’ve raised their defenses sky-high."

  """)
    input("Press Enter To Return To The Menu")

def vocabulary26():
    print("\n-- Vocabulary ---")
    vocabulary_dict = {
        "---Basics of Security Awareness---"
        ""
        "Security Awareness": "The training and education programs that teach employees to recognize and avoid security threats.",
        "Social Engineering Resistance": "Awareness of tricks like phishing, impersonation, and baiting to avoid falling for them.",

        "---Key Elements--"
        ""
        "Phishing Detection": "Training employees to identify fake emails, links, and attachments.",
        "Strong Password Practices": "Encouraging the use of unique, complex passwords and avoiding password reuse.",
        "Reporting Suspicious Activity": "Ensuring employees escalate any unusual behavior or incidents immediately.",
        "Device Security": "Promoting secure practices, such as locking devices and avoiding public Wi-Fi.",
        "Access Control Awareness": "Teaching employees not to share credentials or allow unauthorized access to secure areas.",

        "---Challenges and Weak Points---"
        ""
        "Training Gaps": "Employees who missed or poorly understood training sessions.",
        "Carelessness": "Mistakes or lapses in judgment that compromise security.",
        "Overconfidence": "Employees who believe they’re immune to social engineering, making them easier to fool.",
        "Fatigue": "Reduced vigilance due to frequent drills or constant security alerts.",

        "---Exploitation Strategies---"
        ""
        "Craft Convincing Phishing Attacks": "Creating fake emails and links that appear authentic.",
        "Target the Least Trained": "Focusing on newer or less experienced employees who may lack awareness.",
        "Exploit Carelessness": "Taking advantage of lapses in attention, like unlocked devices or shared credentials.",
        "Overload Their Awareness": "Bombarding staff with distractions to reduce their focus on real threats.",
     }
    
    for term, definition in vocabulary_dict.items():
        print(f"{term}: {definition}")
    input("\nPress Enter to return to the Menu.")

    input("Press Enter to return to the submenu.")

 #####################################################################################################
   

def display_menu():
    
        print("\n--- Menu ---")
        print("=" * 40)
        print("1. Fundamentals of Security")
        print("2. Threat Actors ")
        print("3. Physical Security")
        print("4. Social Engineering" )
        print("5. Malware")
        print("6. Data Protection")
        print("7. Cryptographic Solutions")
        print("8. Risk Management")
        print("9. Third-Party Vendor Risk")
        print("10. Governance and Compliance")
        print("11. Asset and Change Management")
        print("12. Audits and Assesments")
        print("13. Cyber Reseliance and Redundancy")
        print("14. Security Architecture")
        print("15. Security Infrastructure")
        print("16. Identity And Access Management Solutions (IAM)")
        print("17.Vulnerabilities And Attacks")
        print("18. Malicious Activity")
        print("19. Hardening")
        print("20. Security Techniques")
        print("21. Vulnerability Management")
        print("22. Alerting And Monitoring")
        print("23. Incident Response")
        print("24. Investigating an Incident")
        print("25. Automation And Orchestration")
        print("26. Security Awareness")
        print("=" * 40)

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1-26): ").strip()

        if choice == "1":
            print("\nFundamentals Of Secutiy")
            submenu1()
        elif choice == "2":
            submenu2()
            print("\nThreat Actors")
        elif choice == "3":
            print("\nPhysical Security")
            submenu3()
        elif choice == "4":
            print("\nSocial Engineering")
            submenu4()
        elif choice == "5":
            print("\nMalware")
            submenu5()
        elif choice == "6":
            print("\nData Protection")
            submenu6()
        elif choice == "7":
            print("\nCryptographic Solutions")
            submenu7()
        elif choice == "8":
            print("\nRisk Management")
            submenu8()
        elif choice == "9":
            print("\nThird-Party Vendor Risk")
            submenu9()
        elif choice == "10":
            print("\nGovernance and Compliance")
            submenu10()
        elif choice == "11":
            print("\nAsset and Change Management")
            submenu11()
        elif choice == "12":
            print("\nAudits and Assesments")
            submenu12()
        elif choice == "13":
            print("\nCyber Reseliance and Redundancy")
            submenu13()
        elif choice == "14":
            print("\nSecurity Architecture")
            submenu14()
        elif choice == "15":
            print("\nSecurity Infrastructure")
            submenu15()
        elif choice == "16":
            print("\nIdentity And Access Management Solutions (IAM)")
            submenu16()
        elif choice == "17":
            print("\nVulnerabilities And Attacks")
            submenu17()
        elif choice == "18":
            print("\nMalicious Activity")
            submenu18()
        elif choice == "19":
            print("\nHardening")
            submenu19()
        elif choice == "20":
            print("\nSecurity Techniques")
            submenu20()
        elif choice == "21":
            print("\nVulnerability Management")
            submenu21()
        elif choice == "22":
            print("\nAlerting And Monitoring")
            submenu22()
        elif choice == "23":
            print("\nIncident Response")
            submenu23()
        elif choice == "24":
            print("\nInvestigating an Incident")
            submenu24()
        elif choice == "25":
            print("\nAutomation And Orchestration")
            submenu25()
        elif choice == "26":
            print("\nSecurity Awareness")
            submenu26()
