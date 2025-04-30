import tkinter as tk
from tkinter import simpledialog, messagebox
from scapy.all import sniff, IP, TCP, get_if_list
import threading

blocked_ips = set()
blocked_ports = set()
monitoring = False
selected_interface = None

# GUI root for thread-safe UI calls
root = tk.Tk()
root.title("Python Firewall GUI")

# Thread-safe log appending
def safe_log(message):
    log_text.after(0, lambda: log_text_insert(message))

def log_text_insert(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

# Packet processing
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        if TCP in packet:
            dst_port = packet[TCP].dport

            if src_ip in blocked_ips:
                safe_log(f"[BLOCKED IP] {src_ip} ➡ {dst_ip}:{dst_port}")
            elif dst_port in blocked_ports:
                safe_log(f"[BLOCKED PORT] {src_ip} ➡ {dst_ip}:{dst_port}")
            else:
                safe_log(f"[ALLOWED] {src_ip} ➡ {dst_ip}:{dst_port}")

# Sniffing wrapper with stop support
def sniff_packets():
    sniff(prn=packet_callback, store=0, iface=selected_interface, stop_filter=lambda x: not monitoring)

def start_sniffing():
    global monitoring
    if not selected_interface:
        messagebox.showwarning("No Interface", "Please select a network interface first.")
        return
    if monitoring:
        return
    monitoring = True
    sniff_thread = threading.Thread(target=sniff_packets)
    sniff_thread.daemon = True
    sniff_thread.start()

def stop_sniffing():
    global monitoring
    monitoring = False
    safe_log("[INFO] Monitoring stopped.")

def update_blocked_listbox():
    ip_listbox.delete(0, tk.END)
    for ip in blocked_ips:
        ip_listbox.insert(tk.END, ip)

    port_listbox.delete(0, tk.END)
    for port in blocked_ports:
        port_listbox.insert(tk.END, port)

def add_ip():
    ip = simpledialog.askstring("Add IP", "Enter IP to block:")
    if ip:
        blocked_ips.add(ip)
        update_blocked_listbox()

def remove_ip():
    selected = ip_listbox.curselection()
    if selected:
        ip = ip_listbox.get(selected)
        blocked_ips.discard(ip)
        update_blocked_listbox()

def add_port():
    port = simpledialog.askinteger("Add Port", "Enter port to block:")
    if port is not None:
        blocked_ports.add(port)
        update_blocked_listbox()

def remove_port():
    selected = port_listbox.curselection()
    if selected:
        port = int(port_listbox.get(selected))
        blocked_ports.discard(port)
        update_blocked_listbox()

def choose_interface():
    global selected_interface
    interfaces = get_if_list()
    choice = simpledialog.askinteger("Select Interface", "\n".join(f"{i}: {iface}" for i, iface in enumerate(interfaces)))
    if choice is not None and 0 <= choice < len(interfaces):
        selected_interface = interfaces[choice]
        interface_label.config(text=f"Selected: {selected_interface}")

# GUI layout

# Interface selection
tk.Button(root, text="Select Network Interface", command=choose_interface).pack()
interface_label = tk.Label(root, text="No Interface Selected")
interface_label.pack()

# IP controls
tk.Label(root, text="Blocked IPs").pack()
ip_listbox = tk.Listbox(root)
ip_listbox.pack()
tk.Button(root, text="Add IP", command=add_ip).pack()
tk.Button(root, text="Remove Selected IP", command=remove_ip).pack()

# Port controls
tk.Label(root, text="Blocked Ports").pack()
port_listbox = tk.Listbox(root)
port_listbox.pack()
tk.Button(root, text="Add Port", command=add_port).pack()
tk.Button(root, text="Remove Selected Port", command=remove_port).pack()

# Packet log
tk.Label(root, text="Firewall Log").pack()
log_text = tk.Text(root, height=10)
log_text.pack()

# Controls
tk.Button(root, text="Start Monitoring", command=start_sniffing).pack()
tk.Button(root, text="Stop Monitoring", command=stop_sniffing).pack()
tk.Button(root, text="Exit", command=root.destroy).pack()

root.mainloop()
