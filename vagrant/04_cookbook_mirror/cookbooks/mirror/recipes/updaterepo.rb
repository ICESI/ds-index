template "/etc/yum.repos.d/CentOS-Base.repo" do
	source "CentOS-Base.repo.erb"
	mode 0644
	owner "root"
	group "wheel"
	variables(
		:ip_mirror => "#{node[:aptmirror][:server]}"
	)
end
