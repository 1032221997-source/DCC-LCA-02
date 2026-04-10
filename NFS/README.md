# NFS Setup — Commands + Motto

## Installation
```bash
sudo apt update
```
**Motto**: Refresh package list (know what’s available)

```bash
sudo apt install nfs-kernel-server -y
```
**Motto**: Install NFS server (share files)

```bash
sudo apt install nfs-common -y
```
**Motto**: Install NFS client (access shared files)

## 📁 Create Shared Directory (Server)
```bash
sudo mkdir -p /nfs/shared
```
**Motto**: Create a folder to share

```bash
sudo chown nobody:nogroup /nfs/shared
```
**Motto**: Give neutral ownership (avoid permission issues)

```bash
sudo chmod 777 /nfs/shared
```
**Motto**: Allow everyone access (easy setup, not secure)

## Configure Sharing
```bash
sudo nano /etc/exports
```
**Motto**: Define what to share and with whom

Add:
```
/nfs/shared *(rw,sync,no_subtree_check,no_root_squash)
```
**Motto of options**:
- `*` → allow all clients
- `rw` → read & write
- `sync` → write immediately (safe)
- `no_subtree_check` → faster, fewer checks
- `no_root_squash` → root stays root (powerful, risky)

## Apply Configuration
```bash
sudo exportfs -ra
```
**Motto**: Reload exports (apply changes)

```bash
sudo systemctl restart nfs-kernel-server
```
**Motto**: Restart NFS service (make it active)

```bash
sudo exportfs -v
```
**Motto**: Verify what is being shared

## Client Setup
```bash
sudo mkdir -p /mnt/nfs
```
**Motto**: Create mount point (where share appears)

```bash
sudo mount localhost:/nfs/shared /mnt/nfs
```
**Motto**: Connect to NFS share

## Testing
```bash
echo "Hello from Client" | sudo tee /mnt/nfs/client.txt
```
**Motto**: Write file from client (test write access)

```bash
ls /mnt/nfs
```
**Motto**: Check client view

```bash
ls /nfs/shared
```
**Motto**: Check server view

##  Optional (Fix / Reset)
```bash
sudo umount /mnt/nfs
```
**Motto**: Disconnect share

```bash
sudo exportfs -ua
```
**Motto**: Unexport all shares
